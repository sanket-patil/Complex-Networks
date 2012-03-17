/*
 * ==============================================================
 * clustering_coefficients_mex.c The mex interface to the matlab bgl wrapper.
 *
 * David Gleich
 * 23 April 20020
 * =============================================================
 */

/*
 * 19 February 2007
 * Updated to use Matlab 2006b sparse matrix interface
 */


#include "mex.h"

#if MX_API_VER < 0x07030000
typedef int mwIndex;
typedef int mwSize;
#endif // MX_API_VER

#include "matlab_bgl.h"

#include <math.h>
#include <stdlib.h>

/*
 * The mex function runs a clustering coefficients problem.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{   
    int mrows, ncols;
    
    int n,nz;
    
    /* sparse matrix */
    mwIndex *ia, *ja;
    
    /* output data */
    double *ccfs;

    
    if (nrhs != 1) 
    {
        mexErrMsgTxt("1 inputs required.");
    }

    /* The first input must be a sparse matrix. */
    mrows = mxGetM(prhs[0]);
    ncols = mxGetN(prhs[0]);
    if (mrows != ncols ||
        !mxIsSparse(prhs[0])) 
    {
        mexErrMsgTxt("Input must be a noncomplex square sparse matrix.");
    }
    
    n = mrows;
        
    
    /* Get the sparse matrix */
    
    /* recall that we've transposed the matrix */
    ja = mxGetIr(prhs[0]);
    ia = mxGetJc(prhs[0]);
    
    nz = ia[n];
    
    
    plhs[0] = mxCreateDoubleMatrix(n,1,mxREAL);
    
    ccfs = mxGetPr(plhs[0]);
    
    #ifdef _DEBUG
    mexPrintf("clustering_coefficients...");
    #endif 
    
    clustering_coefficients(n, ja, ia,
        ccfs);
    
    
    #ifdef _DEBUG
    mexPrintf("done\n");
    #endif 
    
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

