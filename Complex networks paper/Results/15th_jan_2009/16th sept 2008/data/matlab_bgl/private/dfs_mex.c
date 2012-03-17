/*
 * ==============================================================
 * bfs_mex.c The mex interface to the matlab bgl wrapper.
 *
 * David Gleich
 * 20 April 20020
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
    int full;
    
    /* output data */
    double *d, *dt, *ft, *pred;
    
    int *int_d;
    int *int_dt;
    int *int_ft;
     
    
    if (nrhs != 3) 
    {
        mexErrMsgTxt("3 inputs required.");
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
    full = (int)mxGetScalar(prhs[2]);
    
    plhs[0] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[1] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[2] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[3] = mxCreateDoubleMatrix(1,n,mxREAL);
    
    d = mxGetPr(plhs[0]);
    dt = mxGetPr(plhs[1]);
    ft = mxGetPr(plhs[2]);
    pred = mxGetPr(plhs[3]);
    
    int_d = (int*)d;
    int_dt = (int*)dt;
    int_ft = (int*)ft;
    
    for (i=0; i < n; i++)
    {
        int_d[i]=-1;
        int_dt[i]=-1;
        int_ft[i]=-1;
    }
    
    int_d[u] = 0;
    
    #ifdef _DEBUG
    mexPrintf("dfs...");
    #endif 
    depth_first_search(n, ja, ia,
        u, full, (int*)d, (int*)dt, (int*)ft, (mwIndex*)pred);
    #ifdef _DEBUG
    mexPrintf("done!\n");
    #endif 
   
    
    expand_int_to_double((int*)d, d, n, 0.0);
    expand_int_to_double((int*)dt, dt, n, 0.0);
    expand_int_to_double((int*)ft, ft, n, 0.0);
    expand_index_to_double_zero_equality((mwIndex*)pred, pred, n, 1.0);
    
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

