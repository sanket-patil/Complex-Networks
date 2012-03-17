


/**
 * @file connected_components.cc
 *
 * Implement the BGL connected_components wrapper.
 */

/*
 * David Gleich
 * 16 April 2006
 */

#include "include/matlab_bgl.h"

#include <yasmic/compressed_row_matrix_graph.hpp>
#include <boost/graph/strong_components.hpp>
#include <yasmic/iterator_utility.hpp>

#include <vector>

int connected_components(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    int ci_value = 1;
	constant_iterator<int> ci(&ci_value), ci_end(&ci_value);

    mbglIndex nzcount = ia[nverts];

    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci, ci_end,
					nverts, nverts, nzcount);

    std::vector<int> component_map(nverts);

    return strong_components(g, 
				make_iterator_property_map(component_map.begin(), 
				get(vertex_index, g)));
    
}


