class GRAPH:
    def __init__(self):
        self.g1 = {}

    def display(self):
        if len(self.g1)!= 0:
            for k,v in self.g1.items():
                print(k," : ",v)
        else:
            print("No vertex in graph")

    def addVertex(self,vertex):
        if vertex not in self.g1:
            self.g1[vertex] = []
        else:
            print("Vertex is already in graph")

    def addEdges(self,vertex1,vertex2):
        if vertex1 in self.g1 and vertex2 in self.g1:
            self.g1[vertex1].append(vertex2)
            self.g1[vertex2].append(vertex1)


    def removeEdges(self,vertex1,vertex2):
          if vertex1 in self.g1 and vertex2 in self.g1:
                    self.g1[vertex1].remove(vertex2)
                    self.g1[vertex2].remove(vertex1)


    def removeVertex(self,vertex):
         if vertex in self.g1:
              for adj_vertex in self.g1[vertex]:
                   self.g1[adj_vertex].remove(vertex)
              del self.g1[vertex]
              return True
         return False

    def bfs_traversing(self,vertex):
         if vertex in self.g1:
              visited = [vertex]
              queue = [vertex]
              while queue:
                   dvertex = queue.pop(0)
                   print(dvertex,end=" ")
                   for adj_vertex in self.g1[dvertex]:
                        if adj_vertex not in visited:
                             visited.append(adj_vertex)
                             queue.append(adj_vertex)
         else:
              print("Vertex doesn't exists")



    def dfs_traversing(self,vertex):
             if vertex in self.g1:
                  visited = [vertex]
                  stack = [vertex]
                  while stack:
                       dvertex = stack.pop()
                       print(dvertex,end=" ")
                       for adj_vertex in self.g1[dvertex]:
                            if adj_vertex not in visited:
                                 visited.append(adj_vertex)
                                 stack.append(adj_vertex)
             else:
                  print("Vertex doesn't exists")

         












gh= GRAPH()
gh.addVertex('A')
gh.addVertex('B')
gh.addVertex('C')
gh.addVertex('D')
gh.addVertex('E')
gh.display()
print()
gh.addEdges('A','B')
gh.addEdges('A','C')
# gh.addEdges('A','D')
gh.addEdges('B','E')
gh.addEdges('C','D')
gh.addEdges('D','E')
gh.addEdges('A','C')
gh.display()
print()
# gh.removeEdges('A','D')
gh.display()
print()
# gh.removeVertex('A')
gh.display()

print("Bredth First Search Traversing")
gh.bfs_traversing('A')
print()
print("Depth First Search Traversing")
gh.dfs_traversing('A')
