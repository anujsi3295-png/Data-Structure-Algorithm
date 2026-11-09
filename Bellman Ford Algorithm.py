class BELLMAN_FORD:
    def __init__(self):
        self.vertex = []
        self.edges = []


    def addVertex(self,v):
        if v not in self.vertex:
            self.vertex.append(v)
        # print(self.vertex)

    def addEdges(self,s,d,w):
        if s in self.vertex and d in self.vertex:
            self.edges.append([s,d,w])
            # print(self.edges)

    def bellman_ford(self,src):
        dict = {i:float('Inf') for i in self.vertex}
        dict[src] = 0

        print(dict)

        # bellman ford algorithm

        for _ in range(len(self.vertex) - 1):
            for s,d,w in self.edges:
                if dict[d] > dict[s] + w:
                 dict[d] > dict[s] + w
        print(dict)




o1 = BELLMAN_FORD()
o1.addVertex('A')
o1.addVertex('B')
o1.addVertex('C')
o1.addVertex('D')
o1.addVertex('E')
o1.addEdges('A','C',6)
o1.addEdges('A','D',6)
o1.addEdges('B','A',3)
o1.addEdges('C','B',1)
o1.addEdges('C','D',2)
o1.addEdges('D','C',1)
o1.addEdges('E','B',4)
o1.addEdges('E','C',2)
o1.bellman_ford('E')

