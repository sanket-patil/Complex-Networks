/*
 * =============================================================
 * ipdouble/subsasgn.c Change the vector/matrix/array in place.
 *
 * David Gleich
 * Stanford University
 * 11 May 2006
 * =============================================================
 */

#include "mex.h"

#include <string.h>

#define NUM_SUPPORTED_DIMS 2

void assign(mxArray* lhs, mxArray* subs, mxArray* rhs)
{
    
    int i,j,k;
    
    double *pr;
    double *pl;
    
    
    
    int ndim;
    int ncells;
    
    const int* size_lhs;
    int n_subs_els;
    int n_lhs_els;
    int n_rhs_els;
    
    /* determines if we step the rhs or not */
    int prstep;
    
    /*
     * Ugh... I hope I can fix this eventually...
     */
    
    mxArray* all_subs[NUM_SUPPORTED_DIMS];
    double *pind[NUM_SUPPORTED_DIMS];
    int subs_dim[NUM_SUPPORTED_DIMS];
    
    
    /* make sure the dimensions agree */
    ndim = mxGetNumberOfDimensions(lhs);
    ncells = mxGetNumberOfElements(subs);
    
    if (ndim < ncells)
        mexErrMsgTxt("Index exceeds matrix dimension.");
    
    if (ndim > NUM_SUPPORTED_DIMS)
        mexErrMsgTxt("Not supported (nice try though)!  "
            "If you want this, send me email and help me implement it.");
    
    /*
     * Damn, I know this code is not good, but I can't be bothered to 
     * think of more efficient code right now and matrices should be 
     * sufficient for 99% of people.
     */
    
    /*
     * If anyone knows how to make it work for general tensors, please
     * help me :-)
     */
    
    
    n_subs_els = 1;
    n_lhs_els = mxGetNumberOfElements(lhs);
    n_rhs_els = mxGetNumberOfElements(rhs);
    
    size_lhs = mxGetDimensions(lhs);
    prstep = n_rhs_els > 1;
    
    /*
     * Make sure we have enough elements
     */
    /*mexPrintf("ndim(rhs) = %i\n", mxGetNumberOfDimensions(rhs));
    mexPrintf("ndim(lhs) = %i\n", mxGetNumberOfDimensions(lhs));
    if (prstep && (mxGetNumberOfElements(subs) != mxGetNumberOfDimensions(rhs)))
    {
        mexErrMsgTxt("Subscripted assignment dimension mismatch.");
    }*/
    
 
    
    {
        for (k=0;k<ncells;k++)
        {
            if (mxIsNumeric(mxGetCell(subs,k)))
            {
                n_subs_els *= mxGetNumberOfElements(mxGetCell(subs,k));
            }
            else
            {
                /* This means they put down ":" */
                
                if (ncells == 1)
                    n_subs_els *= mxGetNumberOfElements(lhs);
                else
                    n_subs_els *= size_lhs[k];
            }
        }
        
        if (n_rhs_els > 1 && n_rhs_els != n_subs_els)
        {
            mexErrMsgTxt("In an assignment A(I) = B, the number of elements in A and B\n"
                "must be the same.");
        }
    }
    
    
    
    pr = mxGetPr(rhs);
    pl = mxGetPr(lhs);
    
    if (ncells == 1)
    {       
        all_subs[0] = mxGetCell(subs,0);
        
        if (mxIsNumeric(all_subs[0]))
        {
            pind[0] = mxGetPr(all_subs[0]);
            
            /* check for out of bounds */
            for (i=0; i < n_subs_els; i++)
            {
                if (pind[0][i]-1 >= n_lhs_els)
                {
                    mexErrMsgTxt("Index exceeds matrix dimensions.");
                }
            }
            
            for (i = 0; i < n_subs_els; i++, pr+=prstep)
            {
                //mexPrintf("Check 5 (%i,%i)...\n", n_subs_els, prstep);
                //mexPrintf("pl[%i] = %f <- %f;  \n", (int)pind[0][i]-1, pl[(int)pind[0][i]-1], *pr);
                pl[(int)pind[0][i]-1] = *pr;
                //mexPrintf("pl[%i] = %f\n", (int)pind[0][i]-1, pl[(int)pind[0][i]-1]);
            }
        }
        else
        {
            for (i = 0; i < n_lhs_els; i++, pr+=prstep)
            {
                pl[i] = *pr;
            }
        }
    }
    else
    {
        all_subs[0] = mxGetCell(subs,0);
        all_subs[1] = mxGetCell(subs,1);
        
        /* might as well be efficient and handle the (:,:) case ... */
        if (!mxIsNumeric(all_subs[0]) && !mxIsNumeric(all_subs[1]))
        {
            for (i = 0; i < n_lhs_els; i++, pr+=prstep)
            {
                /* mexPrintf("pl[%i] = %f <- %f;  \n", i, pl[i], *pr); */
                pl[i] = *pr;
            }
        }
        else if (mxIsNumeric(all_subs[0]))
        {
            pind[0] = mxGetPr(all_subs[0]);
            subs_dim[0] = mxGetNumberOfElements(all_subs[0]);
            
            /* check for out of bounds */
            for (i=0; i < subs_dim[0]; i++)
            {
                if (pind[0][i]-1 >= size_lhs[0])
                {
                    mexErrMsgTxt("Index exceeds matrix dimensions.");
                }
            }
            
            if (mxIsNumeric(all_subs[1]))
            {
                pind[1] = mxGetPr(all_subs[1]);
                subs_dim[1] = mxGetNumberOfElements(all_subs[1]);
                
                /* check for out of bounds */
                for (i=0; i < subs_dim[1]; i++)
                {
                    if (pind[1][i]-1 >= size_lhs[1])
                    {
                        mexErrMsgTxt("Index exceeds matrix dimensions.");
                    }
                }
                
                /* do the assignment */
                for (j = 0; j < subs_dim[1]; j++)
                {
                    int offset = (int)(pind[1][j]-1)*size_lhs[0];
                
                    for (i = 0; i < subs_dim[0]; i++, pr+=prstep)
                    {
                        pl[offset+(int)(pind[0][i]-1)] = *pr;
                    }
                }
            }
            else
            {
                //mexPrintf("Check 3...\n");
                /* do the assignment */
                for (j = 0; j < size_lhs[1]; j++)
                {
                    int offset = j*size_lhs[0];
                
                    for (i = 0; i < subs_dim[0]; i++, pr+=prstep)
                    {
                        //mexPrintf("pl[%i] = %f <- %f;  \n", offset+(int)pind[0][i]-1, pl[offset+(int)pind[0][i]-1], *pr);
                        pl[offset+(int)(pind[0][i]-1)] = *pr;
                    }
                }
            }
        }
        else
        {
            /* here, we know that all_subs[1] is numeric */
            pind[1] = mxGetPr(all_subs[1]);
            subs_dim[1] = mxGetNumberOfElements(all_subs[1]);
            
            /* check for out of bounds */
            for (i=0; i < subs_dim[1]; i++)
            {
                if (pind[1][i]-1 >= size_lhs[1])
                {
                    mexErrMsgTxt("Index exceeds matrix dimensions.");
                }
            }
            
            for (j=0; j < subs_dim[1]; j++)
            {
                int offset = (int)(pind[1][j]-1)*size_lhs[0];
                
                for (i=0; i < size_lhs[0]; i++, pr+=prstep)
                {
                    pl[offset+i] = *pr;
                }
            }
        }
    }
    
    
    /*
    else
    {
        all_subs[0] = mxGetCell(subs,0);
        all_subs[1] = mxGetCell(subs,1);
    
        if (!mxIsNumeric(all_subs[0]) || !mxIsNumeric(all_subs[1]))
            mexErrMsgTxt("not quite yet...");
    }*/
    
    
}

/*
 * The mex function updates the matrix pointed to by plhs[1].a in place.
 */
void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[])
{
    int buflen;
    int status;
    
    char *indtype;
    
    mxArray* type;
    mxArray* subs;
    
    mxArray* a;
    
    
    if (nrhs != 3)
    {
        mexErrMsgTxt("This function only accepts three inputs");
    }
    
    if (!mxIsClass(prhs[0],"ipdouble"))
        mexErrMsgTxt("Input 1 must be an ipdouble.");
    
    if (!mxIsStruct(prhs[1]))
        mexErrMsgTxt("Input 2 must be a structure.");
    
    type = mxGetField(prhs[1],0,"type");
    subs = mxGetField(prhs[1],0,"subs");
    
    if (!type || !subs)
        mexErrMsgTxt("Input 2 must have a .type and .subs field.");
    
    if (mxIsChar(type) != 1)
        mexErrMsgTxt("S.type must be a string (type).");
    
    /* Input must be a row vector. */
    if (mxGetM(type) != 1)
        mexErrMsgTxt("Input 2 must be a row vector.");
    
    /* Get the length of the input string. */
    buflen = (mxGetM(type) * mxGetN(type)) + 1;
    
    /* Allocate memory for string. */
    indtype = mxCalloc(buflen, sizeof(char));

    status = mxGetString(type, indtype, buflen);
    if (status != 0) 
        mexErrMsgTxt("Not enough space for filename input.");
    
    if (strcmp(indtype,"()") != 0)
        mexErrMsgTxt("Invalid index type (only matrix indices allowed!)");
    
    if (!mxIsCell(subs))
        mexErrMsgTxt("S.subs must be a cell array.");
    
    if (!mxIsDouble(prhs[2]))
        mexErrMsgTxt("Only double values supported right now!");
    
    a = mxGetField(prhs[0],0,"a");
    if (!a)
        mexErrMsgTxt("Input 1 is not a valid ipdouble class.");
    
    if (!mxIsDouble(a))
        mexErrMsgTxt("Input 1 is not a valid ipdouble class (a is not a double).");
      
    assign(a,subs,prhs[2]);
    
    plhs[0] = prhs[0];
}