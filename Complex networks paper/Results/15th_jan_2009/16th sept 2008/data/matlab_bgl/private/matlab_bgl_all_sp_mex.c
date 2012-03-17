/*
 * ==============================================================
 * matlab_bgl_all_sp_mex.c The mex interface to the matlab bgl wrapper.
 *
 * David Gleich
 * 20 April 2006
 * =============================================================
 */

/*
 * 19 February 2007
 * Updated to use Matlab 2006b sparse matrix interface
 *
 * 1 March 2007
 * Updated to get predecessors from floyd warshall and use expand macros
 */


#include "mex.h"

#if MX_API_VER < 0x07030000
typedef int mwIndex;
typedef int mwSize;
#endif // MX_API_VER

#include "matlab_bgl.h"

#include "expand_macros.h"

#include <math.h>
#include <stdlib.h>
#include <string.h>

/*
 * The mex function runs a shortest path problem.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{   
    mwIndex mrows, ncols;
    
    mwIndex n,nz;
    
    /* sparse matrix */
    mwIndex *ia, *ja;
    double *a;
    
    double dinf;
    
    /* output data */
    double *D;
    int rval;
    
    /* sp type string */
    int buflen;
    char *algname;
    int status;
     
    
    if (nrhs != 3) 
    {
        mexErrMsgTxt("3 inputs required.");
    }

    /* The first input must be a sparse matrix. */
    mrows = mxGetM(prhs[0]);
    ncols = mxGetN(prhs[0]);
    if (mrows != ncols ||
        !mxIsSparse(prhs[0]) ||
        !mxIsDouble(prhs[0]) || 
        mxIsComplex(prhs[0])) 
    {
        mexErrMsgTxt("Input must be a noncomplex square sparse matrix.");
    }
    
    n = mrows;
         
    
    /* Get the sparse matrix */
    
    /* recall that we've transposed the matrix */
    ja = mxGetIr(prhs[0]);
    ia = mxGetJc(prhs[0]);
    a = mxGetPr(prhs[0]);
    
    nz = ia[n];
    
    /* Get the uninitialized value */
    dinf = mxGetScalar(prhs[2]);
    
    /* Get the algorithm type */
    
    if (mxIsChar(prhs[1]) != 1)
        mexErrMsgTxt("Input 2 must be a string (algname).");
    
    /* Input must be a row vector. */
    if (mxGetM(prhs[1]) != 1)
        mexErrMsgTxt("Input 2 must be a row vector.");
    
    /* Get the length of the input string. */
    buflen = (mxGetM(prhs[1]) * mxGetN(prhs[1])) + 1;

    /* Allocate memory for input and output strings. */
    algname = mxCalloc(buflen, sizeof(char));

    status = mxGetString(prhs[1], algname, buflen);
    if (status != 0) 
        mexErrMsgTxt("Not enough space for algname input.");
    
    plhs[0] = mxCreateDoubleMatrix(n,n,mxREAL);
    
    /* create the output vectors */
    
    D = mxGetPr(plhs[0]);
    
    
    #ifdef _DEBUG
    mexPrintf("all_sp_%s...",algname);
    #endif 
    if (strcmp(algname, "johnson") == 0)
    {
        rval = johnson_all_sp(n, ja, ia, a,
            D, dinf);
    }
    else if (strcmp(algname, "floyd_warshall") == 0)
    {
        double *pred = NULL;
        if (nlhs > 1) {
            plhs[1] = mxCreateDoubleMatrix(n,n,mxREAL);
            pred = mxGetPr(plhs[1]);
        }
        rval = floyd_warshall_all_sp(n, ja, ia, a,
            D, dinf, (mbglIndex*)pred);
        if (pred) {
            expand_index_to_double_zero_equality((mwIndex*)pred, pred, n*n, 1.0);
        }
    }
    else
    {
        mexErrMsgTxt("Unknown algname.");
    }
    #ifdef _DEBUG
    mexPrintf("done!\n");
    #endif 
    
    if (rval != 0)
    {
        mexErrMsgTxt("Negative weight cycle detected, check the input.");
    }
    
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

