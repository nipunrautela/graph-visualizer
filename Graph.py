from GraphInterface import GraphInterface


class Graph(GraphInterface):
    _graph = {}  # Private Variable created by the use of '_'

    # Function to add a New Node to Graph
    def addNode(self, node):
        if node not in self._graph:
            self._graph[node] = {}

    # Function to add New Edge to Graph
    def addEdge(self, v1, v2, weight):
        if v1 not in self._graph or v2 not in self._graph:
            return False
        self._graph[v1][v2] = weight
        self._graph[v2][v1] = weight

    # Function to Delete a Pre-existing Node
    def deleteNode(self, node):
        if node not in self._graph:
            return False
        del self._graph[node]
        for i in self._graph:
            if node in self._graph[i]:
                del self._graph[i][node]

    # Function to Delete a Pre-Existing Edge
    def deleteEdge(self, v1, v2):
        if v1 not in self._graph or v2 not in self._graph or v2 not in self._graph[v1] or v1 not in self._graph[v2]:
            return False
        del self._graph[v1][v2]
        del self._graph[v2][v1]

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

    def bfs(visited, graph, node):
        visited = [] 
        queue = []
        path=[]
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            path.append(s)

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return path
            
    def dfs_non(self,graph, source):
       path = []
       stack = [source]
       while(len(stack) != 0):
           s = stack.pop()
           if s not in path:
               path.append(s)
           if s not in graph:
               continue
           for neighbor in graph[s]:
               stack.append(neighbor)
       return path

    def updateWeight(self, v1, v2, weight):
        self._graph[v1][v2] = weight
        self._graph[v2][v1] = weight

    def FindShortestPath(self, start, destination):
        pass

    @property
    def graph(self):
        return self._graph
