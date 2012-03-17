/**
 * @file searches.cc
 *
 * Implement the BGL dfs and bfs wrappers.
 */

/*
 * David Gleich
 * 19 April 2006
 */

#include "include/matlab_bgl.h"

#include <yasmic/compressed_row_matrix_graph.hpp>
#include <yasmic/iterator_utility.hpp>
#include <boost/graph/depth_first_search.hpp>
#include <boost/graph/breadth_first_search.hpp>
#include <boost/graph/visitors.hpp>
#include <boost/graph/astar_search.hpp>
#include <utility>

#include "visitor_macros.hpp"


int breadth_first_search(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    mbglIndex src, /* problem data */
    int* d, int* dt, mbglIndex* pred /* output data: distance, discover time, predecessor */
    )
{
    using namespace yasmic;
    using namespace boost;
    using namespace std;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    mbglIndex nzcount = ia[nverts];
    
    int ci_value = 1;
	constant_iterator<int> ci(&ci_value), ci_end(&ci_value);

    // create the graph g
    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci, ci_end,
					nverts, nverts, nzcount);

    if (!d || !dt || !pred)
    {
        return (-1);
    }

    // set the predecessor to itself
    for (mbglIndex i = 0; i < nverts; i++)
    {
        pred[i] = i;
    }

    int time = 0;

    boost::breadth_first_search(g, src,
                boost::visitor(make_bfs_visitor(
                    make_pair(record_distances(d, on_tree_edge()),
                    make_pair(stamp_times(dt, time, on_discover_vertex()),
                              record_predecessors(pred, on_tree_edge()))))));

    return (0);
}

struct stop_bfs {}; // stop dfs exception

template <class Graph>
struct c_bfs_visitor
{
    bfs_visitor_funcs_t *vis;

    VISITOR_VERTEX_FUNC(initialize_vertex, stop_bfs)
    VISITOR_VERTEX_FUNC(examine_vertex, stop_bfs)
    VISITOR_VERTEX_FUNC(discover_vertex, stop_bfs)
    VISITOR_VERTEX_FUNC(finish_vertex, stop_bfs)

    VISITOR_EDGE_FUNC(examine_edge, stop_bfs)
    VISITOR_EDGE_FUNC(tree_edge, stop_bfs)
    VISITOR_EDGE_FUNC(non_tree_edge, stop_bfs)
    VISITOR_EDGE_FUNC(gray_target, stop_bfs)
    VISITOR_EDGE_FUNC(black_target, stop_bfs)
};


int breadth_first_search_visitor(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    mbglIndex src, /* problem data */
    bfs_visitor_funcs_t vis /* visitor */
    )
{
    using namespace yasmic;
    using namespace boost;
    using namespace std;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    mbglIndex nzcount = ia[nverts];
    
    int ci_value = 1;
	constant_iterator<int> ci(&ci_value), ci_end(&ci_value);

    c_bfs_visitor<crs_graph> visitor;
    visitor.vis = &vis;

    // create the graph g
    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci, ci_end,
					nverts, nverts, nzcount);

    boost::breadth_first_search(g, src,
        boost::visitor(visitor));

    return (0);
}



int depth_first_search(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    mbglIndex src, int full, /* problem data */
    int* d, int* dt, int *ft, mbglIndex *pred /* output data: discover time, finish time, predecessor */
    )
{
    using namespace yasmic;
    using namespace boost;
    using namespace std;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    mbglIndex nzcount = ia[nverts];
    
    int ci_value = 1;
	constant_iterator<int> ci(&ci_value), ci_end(&ci_value);

    // create the graph g
    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci, ci_end,
					nverts, nverts, nzcount);

    if (!d || !dt || !ft || !pred)
    {
        return (-1);
    }

    // set the predecessor to itself
    for (mbglIndex i = 0; i < nverts; i++)
    {
        pred[i] = i;
    }

    int time=0;

    if (!full)
    {
        std::vector<default_color_type> color_vec(num_vertices(g));
        default_color_type c = white_color; // avoid warning about un-init
        
        // call visit because they don't want the full dfs
        boost::depth_first_visit(g, src,
                    make_dfs_visitor(
                        make_pair(record_distances(d, on_tree_edge()),
                        make_pair(stamp_times(dt, time, on_discover_vertex()),
                        make_pair(stamp_times(ft, time, on_finish_vertex()),
                                  record_predecessors(pred, on_tree_edge()))))),
            make_iterator_property_map(color_vec.begin(),
                get(vertex_index,g)));
    }
    else
    {
        // call search because they want the full dfs
        boost::depth_first_search(g, 
                    boost::visitor(make_dfs_visitor(
                        make_pair(record_distances(d, on_tree_edge()),
                        make_pair(stamp_times(dt, time, on_discover_vertex()),
                                  record_predecessors(pred, on_tree_edge()))))));
    }
    return (0);
}

struct stop_dfs {}; // stop dfs exception

template <class Graph>
struct c_dfs_visitor
{
    dfs_visitor_funcs_t *vis;

    VISITOR_VERTEX_FUNC(initialize_vertex, stop_dfs)
    VISITOR_VERTEX_FUNC(start_vertex, stop_dfs)
    VISITOR_VERTEX_FUNC(discover_vertex, stop_dfs)
    VISITOR_VERTEX_FUNC(finish_vertex, stop_dfs)

    VISITOR_EDGE_FUNC(examine_edge, stop_dfs)
    VISITOR_EDGE_FUNC(tree_edge, stop_dfs)
    VISITOR_EDGE_FUNC(back_edge, stop_dfs)
    VISITOR_EDGE_FUNC(forward_or_cross_edge, stop_dfs)
};

int depth_first_search_visitor(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, /* connectivity params */
    mbglIndex src, int full, /* problem data */
    dfs_visitor_funcs_t vis)
{
    using namespace yasmic;
    using namespace boost;
    using namespace std;

    typedef compressed_row_matrix<
        mbglIndex*, mbglIndex*, constant_iterator<int>  >
        crs_graph;   

    mbglIndex nzcount = ia[nverts];
    
    int ci_value = 1;
	constant_iterator<int> ci(&ci_value), ci_end(&ci_value);

    // create the graph g
    crs_graph g(
        ia, ia+nverts+1, ja, ja+nzcount, ci, ci_end,
					nverts, nverts, nzcount);

    c_dfs_visitor<crs_graph> visitor;
    visitor.vis = &vis;

    try
    {
        if (!full)
        {
            std::vector<default_color_type> color_vec(num_vertices(g));
            default_color_type c = white_color; // avoid warning about un-init
            
            // call visit because they don't want the full dfs
            boost::depth_first_visit(g, src,
                visitor,
                make_iterator_property_map(color_vec.begin(),
                    get(vertex_index,g)));
        }
        else
        {
            // call search because they want the full dfs
            boost::depth_first_search(g, 
                        boost::visitor(visitor)
                        );
        }
    }
    catch (stop_dfs) 
    {
    }

    return (0);
}

struct stop_astar {}; // stop astar exception

template <class Graph>
struct c_astar_visitor
{
    astar_visitor_funcs_t *vis;

    VISITOR_VERTEX_FUNC(initialize_vertex, stop_astar)
    VISITOR_VERTEX_FUNC(examine_vertex, stop_astar)
    VISITOR_VERTEX_FUNC(discover_vertex, stop_astar)
    VISITOR_VERTEX_FUNC(finish_vertex, stop_astar)

    VISITOR_EDGE_FUNC(examine_edge, stop_astar)
    VISITOR_EDGE_FUNC(edge_relaxed, stop_astar)
    VISITOR_EDGE_FUNC(edge_not_relaxed, stop_astar)
    VISITOR_EDGE_FUNC(black_target, stop_astar)
};

template <class Graph, class CostType>
class astar_heuristic_data : public std::unary_function<
    typename boost::graph_traits<Graph>::vertex_descriptor, CostType>
{
private:
    CostType *_data;

public:
    typedef typename boost::graph_traits<Graph>::vertex_descriptor Vertex;
    astar_heuristic_data(CostType *data) : _data(data) {}
    CostType operator()(Vertex u) { return _data[u]; }
};

template <class Graph, class CostType>
class astar_heuristic_func : public std::unary_function<
    typename boost::graph_traits<Graph>::vertex_descriptor, CostType>
{
private:
    void *_pdata;
    CostType (*_func)(void *pdata, mbglIndex u);

public:
    typedef typename boost::graph_traits<Graph>::vertex_descriptor Vertex;
    astar_heuristic_func(CostType (*hfunc)(void* pdata, mbglIndex u), void* pdata) : _func(hfunc), _pdata(pdata) {}
    CostType operator()(Vertex u) { return _func(_pdata, u); }
};


int astar_search(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* start vertex */
    double *d, mbglIndex *pred, double *f, /* output */ 
    double *h /* heuristic function value for all vertices */, double dinf)
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

    astar_heuristic_data<crs_weighted_graph,double> hdata(h);

    astar_search(g, src, hdata, 
        distance_inf(dinf).predecessor_map(pred).rank_map(f).distance_map(d));

    return (0);
}

int astar_search_hfunc(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* start vertex */
    double *d, mbglIndex *pred, double *f, 
    double (*hfunc)(void* pdata, mbglIndex u) /* heuristic function */, void* pdata, double dinf)
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

    astar_heuristic_func<crs_weighted_graph,double> h(hfunc, pdata);

    astar_search(g, src, h, 
        distance_inf(dinf).predecessor_map(pred).rank_map(f).distance_map(d));

    return (0);
}

int astar_search_hfunc_visitor(
    mbglIndex nverts, mbglIndex *ja, mbglIndex *ia, double *weight, /* connectivity params */
    mbglIndex src, /* start vertex */
    double *d, mbglIndex *pred, double *f, 
    double (*hfunc)(void* pdata, mbglIndex u) /* heuristic function */, void* pdata, double dinf, 
    astar_visitor_funcs_t vis)
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

    astar_heuristic_func<crs_weighted_graph,double> h(hfunc, pdata);

    c_astar_visitor<crs_weighted_graph> visitor_impl;
    visitor_impl.vis = &vis;

    try
    {
        astar_search(g, src, h, 
            distance_inf(dinf).predecessor_map(pred).rank_map(f).distance_map(d).visitor(visitor_impl));
    }
    catch (stop_astar) 
    {
    }

    return (0);
}
