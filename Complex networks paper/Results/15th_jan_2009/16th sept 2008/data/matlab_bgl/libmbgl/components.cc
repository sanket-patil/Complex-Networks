/**
 * @file components.cc
 *
 * Implement the BGL biconnected_components wrapper.
 */

/*
 * David Gleich
 * 19 April 2006
 */

#include "include/matlab_bgl.h"

#include <yasmic/compressed_row_matrix_graph.hpp>
#include <yasmic/iterator_utility.hpp>
#include <boost/graph/biconnected_components.hpp>
#include <boost/graph/strong_components.hpp>

int strong_components(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    mbglIndex* ci)
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

    strong_components(g,
        make_iterator_property_map(
            ci, get(vertex_index,g)));

    return (0);
}

int biconnected_components(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    mbglIndex* a, mbglIndex* ci)
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

    if (a)
    {
        if (ci)
        {
            std::size_t num_bicomps;
            mbglIndex *oi;
            boost::tie(num_bicomps, oi) =
                biconnected_components(g, 
                    make_iterator_property_map(ci, get(edge_index,g)),
                    a);
        }
        else
        {
            articulation_points(g, a);
        }
    }
    else
    {
        std::size_t num_bicomps = 
            biconnected_components(g, 
                    make_iterator_property_map(ci, get(edge_index,g)));
    }

    return (0);
}

