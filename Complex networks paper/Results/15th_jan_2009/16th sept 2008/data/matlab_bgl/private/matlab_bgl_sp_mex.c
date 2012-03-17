/*
 * ==============================================================
 * matlab_bgl_sp_mex.c The mex interface to the matlab bgl wrapper.
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
#include "visitor_macros.h"
#include "expand_macros.h"

#include <math.h>
#include <stdlib.h>
#include <string.h>

PROTOTYPE_VISITOR_VERTEX_FUNCTION(initialize_vertex)
PROTOTYPE_VISITOR_VERTEX_FUNCTION(examine_vertex)
PROTOTYPE_VISITOR_VERTEX_FUNCTION(discover_vertex)
PROTOTYPE_VISITOR_VERTEX_FUNCTION(finish_vertex)

PROTOTYPE_VISITOR_EDGE_FUNCTION(examine_edge)
PROTOTYPE_VISITOR_EDGE_FUNCTION(edge_relaxed)
PROTOTYPE_VISITOR_EDGE_FUNCTION(edge_not_relaxed)
PROTOTYPE_VISITOR_EDGE_FUNCTION(edge_minimized)
PROTOTYPE_VISITOR_EDGE_FUNCTION(edge_not_minimized)

/*
 * The mex function runs a shortest path problem.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{
    mwIndex i;
    
    mwIndex mrows, ncols;
    
    mwIndex n,nz;
    
    /* sparse matrix */
    mwIndex *ia, *ja;
    double *a;
    
    /* source/sink */
    mwIndex u;
    
    double dinf;
    
    /* true if this function was called with a visitor */
    int use_visitor = 0;
    
    /* output data */
    double *d, *pred;
    
    /* sp type string */
    int buflen;
    char *algname;
    int status;
     
    
    if (nrhs < 4 || nrhs > 5) 
    {
        mexErrMsgTxt("4 or 5 inputs required.");
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
    
    /* The 5th input must be a structure. */
    if (nrhs == 5 && !mxIsStruct(prhs[4]))
    {
        mexErrMsgTxt("Invalid structure.");
    }

    if (nrhs == 5)
    {
        use_visitor = 1;
    }
    
    n = mrows;
         
    
    /* Get the sparse matrix */
    
    /* recall that we've transposed the matrix */
    ja = mxGetIr(prhs[0]);
    ia = mxGetJc(prhs[0]);
    a = mxGetPr(prhs[0]);
    
    nz = ia[n];
    
    /* Get the scalar */
    u = (mwIndex)mxGetScalar(prhs[1]);
    u = u-1;
    
    /* Get the uninitialized value */
    dinf = mxGetScalar(prhs[3]);
    
    /* Get the algorithm type */
    
    if (mxIsChar(prhs[2]) != 1)
        mexErrMsgTxt("Input 3 must be a string (algname).");
    
    /* Input must be a row vector. */
    if (mxGetM(prhs[2]) != 1)
        mexErrMsgTxt("Input 3 must be a row vector.");
    
    /* Get the length of the input string. */
    buflen = (mxGetM(prhs[2]) * mxGetN(prhs[2])) + 1;

    /* Allocate memory for input and output strings. */
    algname = mxCalloc(buflen, sizeof(char));

    status = mxGetString(prhs[2], algname, buflen);
    if (status != 0) 
        mexErrMsgTxt("Not enough space for algname input.");
    
    plhs[0] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[1] = mxCreateDoubleMatrix(1,n,mxREAL);
    
    /* create the output vectors */
    
    d = mxGetPr(plhs[0]);
    pred = mxGetPr(plhs[1]);
    
    
    #ifdef _DEBUG
    mexPrintf("sp_%s...",algname);
    #endif 
    if (strcmp(algname, "dijkstra") == 0)
    {
        if (use_visitor)
        {
            const mxArray *vis = prhs[4];
            dijkstra_visitor_funcs_t d_vis = {0};
    
            /* Check the visitor and construct the visitor structure. */
            d_vis.pdata = (void*)vis;
            CHECK_AND_SET_VISITOR_FUNCTION(vis,initialize_vertex,d_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,discover_vertex,d_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,examine_vertex,d_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,finish_vertex,d_vis);
            
            CHECK_AND_SET_VISITOR_FUNCTION(vis,examine_edge,d_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_relaxed,d_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_not_relaxed,d_vis);
            
            dijkstra_sp_visitor(n, ja, ia, a,
                u,
                d, (mwIndex*)pred, dinf, d_vis);
        }
        else
        {
            dijkstra_sp(n, ja, ia, a,
                u,
                d, (mwIndex*)pred, dinf);
        }
    }
    else if (strcmp(algname, "bellman_ford") == 0)
    {
        if (use_visitor)
        {
            const mxArray *vis = prhs[4];
            bellman_ford_visitor_funcs_t bf_vis = {0};
    
            /* Check the visitor and construct the visitor structure. */
            bf_vis.pdata = (void*)vis;
            CHECK_AND_SET_VISITOR_FUNCTION(vis,initialize_vertex,bf_vis);
            
            CHECK_AND_SET_VISITOR_FUNCTION(vis,examine_edge,bf_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_relaxed,bf_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_not_relaxed,bf_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_minimized,bf_vis);
            CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_not_minimized,bf_vis);
            
            bellman_ford_sp_visitor(n, ja, ia, a,
            u,
            d, (mwIndex*)pred, dinf, bf_vis);
        }
        else
        {
            bellman_ford_sp(n, ja, ia, a,
            u,
            d, (mwIndex*)pred, dinf);
        }
        
    }
    else if (strcmp(algname, "dag") == 0)
    {
        if (use_visitor) { mexWarnMsgTxt("Visitor ignored."); }
        dag_sp(n, ja, ia, a,
            u,
            d, (mwIndex*)pred, dinf);
    }
    else
    {
        mexErrMsgTxt("Unknown algname.");
    }
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
    
    expand_index_to_double_zero_equality((mwIndex*)pred, pred, n, 1.0);
   
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}



CALL_MATLAB_VERTEX_VISITOR_FUNCTION(initialize_vertex)
CALL_MATLAB_VERTEX_VISITOR_FUNCTION(examine_vertex)
CALL_MATLAB_VERTEX_VISITOR_FUNCTION(discover_vertex)
CALL_MATLAB_VERTEX_VISITOR_FUNCTION(finish_vertex)

CALL_MATLAB_EDGE_VISITOR_FUNCTION(examine_edge)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(edge_relaxed)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(edge_not_relaxed)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(edge_minimized)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(edge_not_minimized)

