class GRAPH:
    def __init__(self,vertices):
        self.vertices = vertices
        # print(self.vertices)
        self.resultant = [[0]*len(self.vertices) for _ in range(len(self.vertices))]
        # print(self.resultant)


    def display(self):
        print(" ",end=" ")
        for i in self.vertices:
            print(i,end=" ")
        print()
        for i in range(len(self.vertices)):
            print(self.vertices[i],end=" ")
            for j in self.resultant[i]:
                print(j,end=" ")
            print()


    def add_edges(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            idx1 = self.vertices.index(v1)
            idx2 = self.vertices.index(v2)
            self.resultant[idx1][idx2] = 1
            self.resultant[idx2][idx1] = 1
            return True
        return False


    def remove_edges(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
                    idx1 = self.vertices.index(v1)
                    idx2 = self.vertices.index(v2)
                    self.resultant[idx1][idx2] = 0
                    self.resultant[idx2][idx1] = 0
                    return True
        return False


val=int(input("Enter the total vertices to add"))
vertices=[input()for i in range(val)]
    

vertices = []
val = int(input("Enter the total vertex to add :"))
for i in range(val):
    vertex = input("Enter the vertex name :")
    vertices.append(vertex)


gh = GRAPH(vertices)
gh.display
print(vertices)
print()
gp.add_edges('A','B')
gp.add_edges('A','C')
gp.add_edges('A','D')
gp.display()