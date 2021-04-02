class Graph:
    def __init__(self,graphDict=None):
        if graphDict == None:
            graphDict = {}
        self.graphDict = graphDict
    
    def get_graph(self):
        return self.graphDict
    
        def set_graph(self,graph):
            self.graphDict = graph
    
    def vertices(self):
        return list(self.graphDict)

    def generate_edges(self):
        edges = []
        for node in self.graphDict:
            for neighbour in self.graphDict[node]:
                edges.append((node, neighbour))
        return edges

    def find_isolated_node(self,node):
        return node in self.graphDict and len(self.graphDict[node]) == 0

    def add_vertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []

    def add_edges(self,edges):
        for i in edges:
            for j in i:
                if i not in self.graphDict:
                    self.add_vertex(str(j))
        for i in edges:
            if str(i[0]) in self.graphDict:
                self.graphDict[str(i[0])].append(str(i[1]))
    
    def __str__(self):
        res = "vertices: "
        for k in self.graphDict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res
            
