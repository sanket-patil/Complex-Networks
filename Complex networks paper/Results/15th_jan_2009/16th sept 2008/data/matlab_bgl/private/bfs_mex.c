/*
 * ==============================================================
 * bfs_mex.c The mex interface to the matlab bgl wrapper.
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
 * Updated to use expand macros
 */


#include "mex.h"

#if MX_API_VER < 0x07030000
typedef int mwIndex;
typedef int mwSize;
#endif // MX_API_VER

#include "matlab_bgl.h"

#include <math.h>
#include <stdlib.h>

#include "expand_macros.h"

/*
 * The mex function runs a max-flow min-cut problem.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{
    mwIndex i;
    
    mwIndex mrows, ncols;
    
    mwIndex n,nz;
    
    /* sparse matrix */
    mwIndex *ia, *ja;
    
    /* source/sink */
    mwIndex u;
    
    /* output data */
    double *d, *dt, *pred;
    int *int_d;
    int *int_dt;
    
    if (nrhs != 2) 
    {
        mexErrMsgTxt("2 inputs required.");
    }

    /* The first input must be a sparse matrix. */
    mrows = mxGetM(prhs[0]);
    ncols = mxGetN(prhs[0]);
    if (mrows != ncols ||
        !mxIsSparse(prhs[0])) 
    {
        mexErrMsgTxt("Input must be a square sparse matrix.");
    }
    
    n = mrows;
        
    /* The second input must be a scalar. */
    if (mxGetNumberOfElements(prhs[1]) > 1 || !mxIsDouble(prhs[1]))
    {
        mexErrMsgTxt("Invalid scalar.");
    }
    
    /* Get the sparse matrix */
    
    /* recall that we've transposed the matrix */
    ja = mxGetIr(prhs[0]);
    ia = mxGetJc(prhs[0]);
    
    nz = ia[n];
    
    /* Get the scalar */
    u = (mwIndex)mxGetScalar(prhs[1]);
    u = u-1;
    
    plhs[0] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[1] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[2] = mxCreateDoubleMatrix(1,n,mxREAL);
    
    d = mxGetPr(plhs[0]);
    dt = mxGetPr(plhs[1]);
    pred = mxGetPr(plhs[2]);
    
    int_d = (int*)d;
    int_dt = (int*)dt;
    
    for (i=0; i < n; i++)
    {
        int_d[i]=-1;
        int_dt[i]=-1;
    }
    
    int_d[u] = 0;
    
    #ifdef _DEBUG
    mexPrintf("bfs...");
    #endif 
    breadth_first_search(n, ja, ia,
        u, (int*)d, (int*)dt, (mbglIndex*)pred);
    #ifdef _DEBUG
    mexPrintf("done!\n");
    #endif 
    
    
    expand_int_to_double((int*)d, d, n, 0.0);
    expand_int_to_double((int*)dt, dt, n, 0.0);
    expand_index_to_double_zero_equality((mwIndex*)pred, pred, n, 1.0);
    
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

