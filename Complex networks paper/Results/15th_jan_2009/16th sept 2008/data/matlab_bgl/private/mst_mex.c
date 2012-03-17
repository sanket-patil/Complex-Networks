/*
 * ==============================================================
 * mst_mex.c The mex interface to the matlab bgl wrapper.
 *
 * David Gleich
 * 20 April 2006
 * =============================================================
 */


/*
 * 10 November 2006:
 * Alterted the code to produce the correct number of edges 
 * in the minimum spanning tree by resizing the arrays.  The previous code
 * had a bug where graphs with disconnected components would have errors 
 * in the edges in the minimum spanning trees.
 *
 * 19 February 2007
 * Updated to use Matlab 2006b sparse matrix interface
 *
 * 1 March 2007
 * Updated to use expand macros
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
 * The mex function runs a MST problem.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{ 
    mwIndex mrows, ncols;
    
    mwIndex n,nz;
    
    /* sparse matrix */
    mwIndex *ia, *ja;
    double *a;
       
    /* output data */
    double *it, *jt, *vt;
    
    /* sp type string */
    int buflen;
    char *algname;
    int status;
    
    mwIndex nedges;
     
    
    if (nrhs != 2) 
    {
        mexErrMsgTxt("2 inputs required.");
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
    
    plhs[0] = mxCreateDoubleMatrix(n-1,1,mxREAL);
    plhs[1] = mxCreateDoubleMatrix(n-1,1,mxREAL);
    plhs[2] = mxCreateDoubleMatrix(n-1,1,mxREAL);
    
    /* create the output vectors */    
    it = mxGetPr(plhs[0]);
    jt = mxGetPr(plhs[1]);
    vt = mxGetPr(plhs[2]);
    
    #ifdef _DEBUG
    mexPrintf("mst_alg_%s...",algname);
    #endif 
    
    nedges = 0;
    if (strcmp(algname, "prim") == 0)
    {
        prim_mst(n, ja, ia, a,
            (mwIndex*)it,(mwIndex*)jt, vt, &nedges);
    }
    else if (strcmp(algname, "kruskal") == 0)
    {
        kruskal_mst(n, ja, ia, a,
            (mwIndex*)it,(mwIndex*)jt, vt, &nedges);
    }
    else
    {
        mexErrMsgTxt("Unknown algname.");
    }
    #ifdef _DEBUG
    mexPrintf("done\n");
    #endif 
    
    expand_index_to_double((mwIndex*)it, it, n-1, 1.0);
    expand_index_to_double((mwIndex*)jt, jt, n-1, 1.0);
    
    /* resize the output to the correct number of edges */
    mxSetM(plhs[0], nedges);
    mxSetM(plhs[1], nedges);
    mxSetM(plhs[2], nedges);
    
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

