/**
 * @file shortest_path.cc
 *
 * Implement the BGL shortest path algorithm wrappers.
 */

/*
 * David Gleich
 * 19 April 2006
 */

#include "include/matlab_bgl.h"

#include <yasmic/compressed_row_matrix_graph.hpp>
#include <yasmic/iterator_utility.hpp>

#include <boost/graph/dijkstra_shortest_paths.hpp>
#include <yasmic/boost_mod/bellman_ford_shortest_paths.hpp>
#include <boost/graph/dag_shortest_paths.hpp>
#include <boost/graph/johnson_all_pairs_shortest.hpp>
//#include <boost/graph/floyd_warshall_shortest.hpp>
#include <yasmic/boost_mod/floyd_warshall_shortest.hpp>

#include "visitor_macros.hpp"

/*
 * Wrapper class to turn a row-storage matrix into 
 * a boost BasicMatrix 
 */
template <class value_type>
struct row_matrix
{
    value_type* head;
    std::size_t nrows;
    std::size_t ncols;
	const value_type* operator[](std::size_t i) const
    {
        return (head+ncols*i);
    }
    
    value_type* operator[](std::size_t i)
    {
    	return (head+ncols*i);
    }

    row_matrix(value_type* _head, std::size_t _nrows, std::size_t _ncols)
        : head(_head), nrows(_nrows), ncols(_ncols)
    {}
};

int dijkstra_sp(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* problem data */
    double* d, mbglIndex *pred, double dinf)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

    dijkstra_shortest_paths(g, src, distance_inf(dinf).predecessor_map(pred).distance_map(d));

    return (0);
}

struct stop_dijkstra {}; // stop dijkstra exception

template <class Graph>
struct c_dijkstra_visitor
{
    dijkstra_visitor_funcs_t *vis;

    VISITOR_VERTEX_FUNC(initialize_vertex, stop_dijkstra)
    VISITOR_VERTEX_FUNC(examine_vertex, stop_dijkstra)
    VISITOR_VERTEX_FUNC(discover_vertex, stop_dijkstra)
    VISITOR_VERTEX_FUNC(finish_vertex, stop_dijkstra)

    VISITOR_EDGE_FUNC(examine_edge, stop_dijkstra)
    VISITOR_EDGE_FUNC(edge_relaxed, stop_dijkstra)
    VISITOR_EDGE_FUNC(edge_not_relaxed, stop_dijkstra)

};

int dijkstra_sp_visitor(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* problem data */
    double* d, mbglIndex *pred, 
    double dinf, dijkstra_visitor_funcs_t vis)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);
    
    c_dijkstra_visitor<crs_weighted_graph> visitor_impl;
    visitor_impl.vis = &vis;

    try
    {
        dijkstra_shortest_paths(g, src, distance_inf(dinf).predecessor_map(pred).distance_map(d).visitor(visitor_impl));
    }
    catch (stop_dijkstra)
    {
    }

    return (0);
}

int bellman_ford_sp(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* problem data */
    double* d, mbglIndex *pred, double dinf)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

    bellman_ford_shortest_paths(g, 
        root_vertex(src).distance_inf(dinf).predecessor_map(pred).distance_map(d));

    return (0);
}

struct stop_bellman_ford {}; // stop dijkstra exception

template <class Graph>
struct c_bellman_ford_visitor
{
    bellman_ford_visitor_funcs_t *vis;

    VISITOR_VERTEX_FUNC(initialize_vertex, stop_bellman_ford)

    VISITOR_EDGE_FUNC(examine_edge, stop_bellman_ford)
    VISITOR_EDGE_FUNC(edge_relaxed, stop_bellman_ford)
    VISITOR_EDGE_FUNC(edge_not_relaxed, stop_bellman_ford)
    VISITOR_EDGE_FUNC(edge_minimized, stop_bellman_ford)
    VISITOR_EDGE_FUNC(edge_not_minimized, stop_bellman_ford)
};

int bellman_ford_sp_visitor(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* problem data */
    double* d, mbglIndex *pred, double dinf,
    bellman_ford_visitor_funcs_t vis)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

    c_bellman_ford_visitor<crs_weighted_graph> visitor_impl;
    visitor_impl.vis = &vis;

    try
    {
        bellman_ford_shortest_paths(g, 
            root_vertex(src).distance_inf(dinf).predecessor_map(pred).distance_map(d).visitor(visitor_impl));
    }
    catch (stop_bellman_ford)
    {
    }

    return (0);
}

int dag_sp(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* problem data */
    double* d, mbglIndex *pred, double dinf)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

    dag_shortest_paths(g, src, 
        distance_inf(dinf).predecessor_map(pred).distance_map(d));

    return (0);
}

int johnson_all_sp(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    double* D, double dinf)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

    row_matrix<double> Dmat(D,nverts,nverts);
    
    bool rval = johnson_all_pairs_shortest_paths(g, Dmat, 
		distance_inf(dinf).distance_combine(std::plus<double>()));

	if (rval == true)
	{
		return (0);
	}
	
	// else, there was an error
	return (-1);
}

int floyd_warshall_all_sp(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    double* D, double dinf,
    mbglIndex* pred)
{
    using namespace yasmic;
    using namespace boost;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, double*  >
        crs_weighted_graph;   

    mbglIndex nzcount = ia[nverts];
    
    // create the graph g
    crs_weighted_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, weight, weight+nzcount,
					nverts, nverts, nzcount);

    row_matrix<double> Dmat(D,nverts,nverts);    
    bool rval = false;
    if (!pred) {
        rval = floyd_warshall_all_pairs_shortest_paths(g, 
            Dmat, distance_inf(dinf).distance_combine(std::plus<double>()));
    } else {
        row_matrix<mbglIndex> Pmat(pred,nverts,nverts);  
        //rval = floyd_warshall_all_pairs_shortest_paths(g, 
        //    Dmat, distance_inf(dinf).distance_combine(std::plus<double>()).predecessor_map(Pmat));
        // making this call is ridiculous, but otherwise, it won't pick up the right type!
        rval = floyd_warshall_all_pairs_shortest_paths(g, Dmat, Pmat, get(edge_weight,g),
            std::less<double>(),std::plus<double>(),dinf,0.0);
    }

	if (rval == true)
	{
		return (0);
	}
	
	// else, there was an error
	return (-1);
}

