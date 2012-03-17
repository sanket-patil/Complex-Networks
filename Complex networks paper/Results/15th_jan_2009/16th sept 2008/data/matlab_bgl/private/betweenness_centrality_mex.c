/*
 * ==============================================================
 * betweenness_centrality_mex.c The mex interface to the matlab bgl wrapper.
 *
 * David Gleich
 * 23 April 2006
 * =============================================================
 */

/*
 * 19 February 2007
 * Updated to use Matlab 2006b sparse matrix interface
 *
 * 22 February 2007 
 * Added edge centrality output
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
 * The mex function runs a betweenness-centrality problem.
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
    double *bc;
    double *ec;
    
    /* used to switch between algorithm types */
    int unweighted;
     
    if (nrhs != 2) 
    {
        mexErrMsgTxt("2 inputs required.");
    }
    
    /* The second input must be a scalar. */
    if (mxGetNumberOfElements(prhs[1]) > 1 || !mxIsDouble(prhs[1]))
    {
        mexErrMsgTxt("Invalid scalar.");
    }
    
    /* get the scalar, because it affects what type of matrices we can look at */
    unweighted = (int)mxGetScalar(prhs[1]);

    /* The first input must be a sparse matrix. */
    mrows = mxGetM(prhs[0]);
    ncols = mxGetN(prhs[0]);
    if (mrows != ncols ||
        !mxIsSparse(prhs[0]) ||
        ((!mxIsDouble(prhs[0]) || mxIsComplex(prhs[0])) && !unweighted)
        )
    {
        mexErrMsgTxt("Input must be a square sparse matrix.");
    }
    
    n = mrows;
         
    
    /* Get the sparse matrix */
    
    /* recall that we've transposed the matrix */
    ja = mxGetIr(prhs[0]);
    ia = mxGetJc(prhs[0]);
    
    nz = ia[n];
    
    
    
    plhs[0] = mxCreateDoubleMatrix(n,1,mxREAL);
    /* create the output vectors */    
    bc = mxGetPr(plhs[0]);

    /* if they requested edge centrality, compute that as well */
    if (nlhs > 1) {
        plhs[1] = mxCreateDoubleMatrix(nz,1,mxREAL);
        ec = mxGetPr(plhs[1]);
    } else {
        ec = NULL;
    }
    
    
    #ifdef _DEBUG
    mexPrintf("betweenness_centrality...");
    #endif 
    
    if (unweighted)
    {
        betweenness_centrality(n, ja, ia, NULL,
            bc, ec);
    }
    else
    {
        a = mxGetPr(prhs[0]);
        betweenness_centrality(n, ja, ia, a,
            bc, ec);
    }
    #ifdef _DEBUG
    mexPrintf("done\n");
    #endif 
    
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

