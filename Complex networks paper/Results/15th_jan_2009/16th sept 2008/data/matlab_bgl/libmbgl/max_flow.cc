


/**
 * @file max_flow.cc
 *
 * Implement the BGL push_relabel_max_flow wrapper.
 */

/*
 * David Gleich
 * 16 April 2006
 */

#include "include/matlab_bgl.h"

#include <yasmic/compressed_row_matrix_graph.hpp>
#include <boost/graph/push_relabel_max_flow.hpp>
#include <yasmic/iterator_utility.hpp>
#include <boost/property_map.hpp>

template <class RowIter, class ColIter, class ValIter, class Child>
struct reverse_edge_pmap_helper
{
    typedef yasmic::compressed_row_matrix<RowIter, ColIter, ValIter> matrix;
    typedef boost::graph_traits<matrix> traits;

    typedef typename traits::edge_descriptor key_type;
    typedef typename traits::edge_descriptor value_type;
    typedef boost::lvalue_property_map_tag category;
    typedef typename traits::edge_descriptor reference;

    typedef boost::put_get_helper<reference, Child> super_class;
};

template <class RowIter, class ColIter, class ValIter>
class reverse_edge_pmap
    : reverse_edge_pmap_helper<RowIter, ColIter, ValIter, 
        reverse_edge_pmap<RowIter, ColIter, ValIter> >::super_class
{
    typedef yasmic::compressed_row_matrix<RowIter, ColIter, ValIter> matrix;
    typedef boost::graph_traits<matrix> traits;

    typedef typename traits::edge_descriptor key_type;
    typedef typename traits::edge_descriptor value_type;
    typedef boost::lvalue_property_map_tag category;
    typedef typename traits::edge_descriptor reference;

    mbglIndex* _rev_edge_index;

public:
    inline reference 
    operator[](key_type v) const 
    {
        return yasmic::make_simple_nonzero(v._row, v._column, v._val, _rev_edge_index[v._nzi]);
    }

    inline 
    reverse_edge_pmap(mbglIndex* rev_edge_index)
    : _rev_edge_index(rev_edge_index)
    {}

    
};

template <class RowIter, class ColIter, class ValIter>
inline reverse_edge_pmap<RowIter, ColIter, ValIter>
make_reverse_edge_pmap(
    const yasmic::compressed_row_matrix<RowIter, ColIter, ValIter>& g,
    mbglIndex* rev_edge_index)
{
    return reverse_edge_pmap<RowIter,ColIter,ValIter>(rev_edge_index);
}

int push_relabel_max_flow(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia,  
    mbglIndex src, mbglIndex sink, 
    int* cap, int* res, 
    mbglIndex* rev_edge_index,
    int* flow)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    mbglIndex nzcount = ia[nverts];

    int ci_value = 1;
	constant_iterator<int> ci(&ci_value), ci_end(&ci_value);

    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci, ci_end,
					nverts, nverts, nzcount);

    *flow = (push_relabel_max_flow(g,
        src, sink,
        make_iterator_property_map(
            cap, get(edge_index,g)),
        make_iterator_property_map(
            res, get(edge_index,g)),
        make_reverse_edge_pmap(g,rev_edge_index),
        get(vertex_index,g)));

    return (0);
}


