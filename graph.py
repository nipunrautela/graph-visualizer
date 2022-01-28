from GraphInterface import GraphInterface


class Graph(GraphInterface):
    _graph = {}  # Private Variable created by the use of '_'

    # Function to add a New Node to Graph
    def addNode(self, node):
        if node not in self._graph:
            self._graph[node] = []

    # Function to add New Edge to Graph
    def addEdge(self, v1, v2):
        if v1 not in self._graph or v2 not in self._graph:
            return False
        self._graph[v1].append(v2)
        self._graph[v2].append(v1)

    # Function to Delete a Pre-existing Node
    def deleteNode(self, node):
        if node not in self._graph:
            return False
        del self._graph[node]
        for i in self._graph:
            for j in self._graph[i]:
                if j == node:
                    self._graph[i].remove(j)

    # Function to Delete a Pre-Existing Edge
    def deleteEdge(self, v1, v2):
        if v1 not in self._graph or v2 not in self._graph or v2 not in self._graph[v1] or v1 not in self._graph[v2]:
            return False
        self._graph[v1].remove(v2)
        self._graph[v2].remove(v1)

    # Function to Get Adjacent Node of a Node
    def getAdjacentNodes(self, v1):
        if v1 not in self._graph:
            return False
        for i in self._graph[v1]:
            print(i, end=" ")
        print()

    # Function to get Adjacent Edges of an Edge
    def getAdjacentEdges(self, v1, v2):
        if v1 not in self._graph or v2 not in self._graph:
            return False
        l = []
        for i in self._graph[v1]:
            if i == v2:
                continue
            l.append((v1, i))
        for i in self._graph[v2]:
            if i == v1:
                continue
            l.append((v2, i))
        return tuple(l)

    @property
    def graph(self):
        return self._graph


graph = Graph()
graph.addNode(0)
graph.addNode(1)
graph.addNode(2)
graph.addNode(3)
graph.addNode(4)
graph.addEdge(0, 1)
graph.addEdge(0, 3)
graph.addEdge(1, 2)
graph.addEdge(3, 2)
graph.addEdge(2, 4)
graph.deleteEdge(0,2)
print(graph.getAdjacentEdges(1, 2))

