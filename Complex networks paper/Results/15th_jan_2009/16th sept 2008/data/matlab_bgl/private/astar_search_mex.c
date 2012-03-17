/*
 * ==============================================================
 * astar_search_mex.c The mex interface to the astar_search 
 * wrapper.
 *
 * David Gleich
 * 31 May 2006
 * =============================================================
 */

/*
 * 19 February 2007
 * Updated to use Matlab 2006b sparse matrix interface
 *
 * 28 February 2007
 * Tried to fix bugs with Matlab 2006b sparse matrix interface.
 */

/*
 * additional documentation for visitor for astar visitor
 *
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
PROTOTYPE_VISITOR_EDGE_FUNCTION(black_target)


#include "expand_macros.h"

/* the heuristic function */
double astar_heuristic(void *pdata, mwIndex u);

/*
 * The mex function runs a shortest path problem.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{
    mwIndex i;
    
    mwIndex mrows, ncols;
    
    mwSize n,nz;
    
    /* sparse matrix */
    mwIndex *ia, *ja;
    double *a;
    
    /* source/sink */
    mbglIndex u;
    
    double dinf;
    
    /* true if this function was called with a visitor */
    int use_visitor = 0;
    
    /* true if this function was called with a vector as h */
    int use_vector = 0;
    
    /* output data */
    double *d, *pred, *f;

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
    u = (mbglIndex)mxGetScalar(prhs[1]);
    u = u-1;
    
    /* Get the uninitialized value */
    dinf = mxGetScalar(prhs[3]);
    
    if (mxIsDouble(prhs[2]))
    {
        if (mxGetNumberOfElements(prhs[2]) != n)
        {
            mexErrMsgTxt("The size of the vector heuristic must be the number of vertices.");
        }
        use_vector = 1;
    }
    else
    {
        int clsId = mxGetClassID(prhs[2]);
        if (!(clsId == mxFUNCTION_CLASS || clsId == 23))
        {
            mexErrMsgTxt("The heuristic must be either a double vector or a function.");
        }
    }
    
    plhs[0] = mxCreateDoubleMatrix(n,1,mxREAL);
    plhs[1] = mxCreateDoubleMatrix(1,n,mxREAL);
    plhs[2] = mxCreateDoubleMatrix(n,1,mxREAL);
    
    /* create the output vectors */
    
    d = mxGetPr(plhs[0]);
    pred = mxGetPr(plhs[1]);
    f = mxGetPr(plhs[2]);
    
    
    #ifdef _DEBUG
    mexPrintf("astar_search...");
    #endif 
    if (use_visitor)
    {
        const mxArray *vis = prhs[4];
        astar_visitor_funcs_t as_vis = {0};

        /* Check the visitor and construct the visitor structure. */
        as_vis.pdata = (void*)vis;
        CHECK_AND_SET_VISITOR_FUNCTION(vis,initialize_vertex,as_vis);
        CHECK_AND_SET_VISITOR_FUNCTION(vis,discover_vertex,as_vis);
        CHECK_AND_SET_VISITOR_FUNCTION(vis,examine_vertex,as_vis);
        CHECK_AND_SET_VISITOR_FUNCTION(vis,finish_vertex,as_vis);

        CHECK_AND_SET_VISITOR_FUNCTION(vis,examine_edge,as_vis);
        CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_relaxed,as_vis);
        CHECK_AND_SET_VISITOR_FUNCTION(vis,edge_not_relaxed,as_vis);
        CHECK_AND_SET_VISITOR_FUNCTION(vis,black_target,as_vis);

        astar_search_hfunc_visitor(n, ja, ia, a,
            u,
            d, (mwIndex*)pred, f, astar_heuristic, (void*)prhs[2], dinf, as_vis);
    }
    else
    {
        if (use_vector)
        {
            astar_search(n, ja, ia, a,
            u,
            d, (mwIndex*)pred, f, mxGetPr(prhs[2]), dinf);
        }
        else
        {
            astar_search_hfunc(n, ja, ia, a,
            u,
            d, (mwIndex*)pred, f, astar_heuristic, (void*)prhs[2], dinf);
        }
    }

    #ifdef _DEBUG
    mexPrintf("done\n");
    #endif 
    
    expand_index_to_double_zero_equality((mwIndex*)pred, pred, n, 1.0);
   
    #ifdef _DEBUG
    mexPrintf("return\n");
    #endif 
}

double astar_heuristic(void *pdata, mwIndex u)
{
    const mxArray *f = pdata;
    
    mxArray* prhs[2]; 
    mxArray* plhs[1]; 
    
    prhs[0] = (void*)f;
    prhs[1] = mxCreateDoubleScalar((double)(u+1)); 
     
    plhs[0] = NULL; 
    mexCallMATLAB(1,plhs,2,prhs,"feval"); 
    
    if (plhs[0] == NULL)
    {
        mexErrMsgTxt("Heuristic function did not return a value.");
    }
    
    /* mexPrintf("h(%i) = %f\n", u, (double)mxGetScalar(plhs[0])); */
    
    return (double)mxGetScalar(plhs[0]);
}

CALL_MATLAB_VERTEX_VISITOR_FUNCTION(initialize_vertex)
CALL_MATLAB_VERTEX_VISITOR_FUNCTION(examine_vertex)
CALL_MATLAB_VERTEX_VISITOR_FUNCTION(discover_vertex)
CALL_MATLAB_VERTEX_VISITOR_FUNCTION(finish_vertex)

CALL_MATLAB_EDGE_VISITOR_FUNCTION(examine_edge)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(edge_relaxed)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(edge_not_relaxed)
CALL_MATLAB_EDGE_VISITOR_FUNCTION(black_target)
