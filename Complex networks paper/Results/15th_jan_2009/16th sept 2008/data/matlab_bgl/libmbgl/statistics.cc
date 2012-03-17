/**
 * @file statistics.cc
 *
 * Implement the graph statistics algorithms.
 */

/*
 * David Gleich
 * 21 April 2006
 */

#include "include/matlab_bgl.h"

#include <yasmic/compressed_row_matrix_graph.hpp>
#include <yasmic/iterator_utility.hpp>

#include <vector>


#include <boost/graph/iteration_macros.hpp>
/* #include <boost/graph/betweenness_centrality.hpp>*/
/* #include "betweenness_centrality.hpp" */
#include <yasmic/boost_mod/betweenness_centrality.hpp>

template <class Vertex, class IndMap>
struct in_indicator_pred
	: public std::unary_function<Vertex, bool>
{
	in_indicator_pred(IndMap indmap, Vertex src)
		: i(indmap), u(src)
	{}

	IndMap i;
    Vertex u;

	bool operator() (const Vertex &v) const
	{   
		return (i[v] > 0) && (u != v);
	}
};

/* Clustering Coefficients Code */
template <class Graph, class CCMap, class IndMap>
void cluster_coefficients(const Graph& g, CCMap cc, IndMap ind)
{
	using namespace boost;

	BGL_FORALL_VERTICES_T(v,g,Graph)
	{
		cc[v] = 0;
		ind[v] = 0;
	}

	
	BGL_FORALL_VERTICES_T(v,g,Graph)
	{
		BGL_FORALL_ADJ_T(v,w,g,Graph)
		{
			ind[w] = 1;
		}

        ind[v] = 0;

		typename property_traits<CCMap>::value_type cur_cc = 0;
		typename graph_traits<Graph>::degree_size_type d = out_degree(v, g);

		

		BGL_FORALL_ADJ_T(v,w,g,Graph)
		{
            // if we are adjacent to ourselves, skip the iteration
            if (v == w) { --d; continue; }

            in_indicator_pred<
    			typename graph_traits<Graph>::vertex_descriptor,
			    IndMap> p(ind,w);

			typename graph_traits<Graph>::adjacency_iterator ai, aiend;
			boost::tie(ai, aiend) = adjacent_vertices(w,g);

			// count if this is in the indicator predicate
			cur_cc += (int)count_if(ai, aiend, p);
		}

        if (d > 1)
        {
		    cc[v] = (double)cur_cc/(double)((d*(d-1)));
        }
        else
        {
            cc[v] = 0.0;
        }

		// reset the indicator
		BGL_FORALL_ADJ_T(v,w,g,Graph)
		{
			ind[w] = 0;
		}
	}
}

int clustering_coefficients(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    double* ccfs)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    mbglIndex nzcount = ia[nverts];
    
    int ci_value = 1;
	constant_iterator<int> ci_begin(&ci_value), ci_end(&ci_value);



    // create the graph g
    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci_begin, ci_end,
					nverts, nverts, nzcount);


    std::vector<mbglIndex> indicator_map(num_vertices(g));

    cluster_coefficients(g,
        make_iterator_property_map(
            ccfs, get(vertex_index,g)),
        make_iterator_property_map(
            indicator_map.begin(), get(vertex_index,g)));

    return (0);
}



int betweenness_centrality(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    double *centrality, double *ecentrality)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   
    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    int ci_value = 1;
	constant_iterator<int> ci_begin(&ci_value), ci_end(&ci_value);

    if (weight)
    {
        // create the weighted graph g
        crs_weighted_graph g(
            ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

        if (ecentrality) {
            brandes_betweenness_centrality(g,
	        		centrality_map(centrality)
                    .weight_map(
                        make_iterator_property_map(weight,
                            get(edge_index,g)))
                    .edge_centrality_map(
                        make_iterator_property_map(
                            ecentrality, get(edge_index, g))));
        } else {
            brandes_betweenness_centrality(g,
	        		centrality_map(centrality)
                    .weight_map(
                        make_iterator_property_map(weight,
                            get(edge_index,g))));
        }
    }
    else
    {
        // create the unweighted graph g
        crs_graph g(
            ia, ia+nverts+1, ja, ja+nzcount, ci_begin, ci_end,
					nverts, nverts, nzcount);

        if (ecentrality) {
            brandes_betweenness_centrality(g,
			    	centrality_map(centrality)
                    .edge_centrality_map(
                        make_iterator_property_map(
                            ecentrality, get(edge_index, g))));
        } else {
            brandes_betweenness_centrality(g,
			    	make_iterator_property_map(centrality, 
				    	get(vertex_index, g)));
        }
    }
    


    return (0);

}


