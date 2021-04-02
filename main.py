import Graph as g



if __name__ == '__main__':
    graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
    G = g.Graph(graph)
    v = G.generate_edges()
    G.add_edges({("b","l"),("b","v"),("v","x")})
    gg = G.get_graph()
    G.visualize_graph()
    # print(G)
