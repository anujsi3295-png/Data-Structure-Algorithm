class Node:
    def __init__(self,data):
        self.data = data 
        self.addr = None 

class Single_Linked_List:
    def __init__(self):
        self.head = None 

    def insert_at_last(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.addr != None:
                temp = temp.addr
            temp.addr = newNode

    def display(self):
        if self.head is None:
            print("No nodes in SLL")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" -> ")
                temp = temp.addr
            print()

    def length(self):
        if self.head is None:
            print("No nodes to count")
        else:
            count = 0
            temp = self.head
            while temp:
                count += 1
                temp = temp.addr
            return count

    def insert_at_first(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.addr = self.head
            self.head = newNode

    def insert_at_loc(self,val,loc):
        newNode = Node(val)
        if loc <= 0:
            print("Enter loc above 0")
        elif loc == 1:
            self.insert_at_first(val)
        elif loc == self.length() + 1:
            self.insert_at_last(val)
        elif loc > self.length():
            print("enter loc lessyhan ->",self.length())
        else:
            temp = self.head
            cnt = 1
            while temp.addr != None and cnt < loc - 1:
                temp = temp.addr
                cnt += 1
            newNode.addr = temp.addr
            temp.addr = newNode

    def delete_at_last(self):
        if self.head is None:
            print("no nodes to delete")
        elif self.length() == 1:
            self.head = None 
        else:
            temp = self.head
            while temp.addr.addr != None:
                temp = temp.addr
            temp.addr = None

    def delete_at_first(self):
        if self.head is None:
            print("No nodes to delete")
        else:
            self.head = self.head.addr

    def delete_at_loc(self,loc):
        if self.head is None:
            print("No nodes to delete")
        elif loc <= 0:
            print("enter location above 0")
        elif loc == 1:
            self.delete_at_first()
        # elif loc == self.length():
        #     self.delete_at_last()
        elif loc > self.length():
            print("enter location lessthan ->",self.length())
        else:
            temp = self.head
            cnt = 1
            while cnt < loc - 1:
                temp = temp.addr
                cnt += 1
            temp.addr = temp.addr.addr

s1 = Single_Linked_List()   
s1.insert_at_last('A')
s1.insert_at_last('B')
s1.insert_at_last('c')
s1.insert_at_last('D')
s1.display()

print("Total nodes in sll ->",s1.length())
s1.insert_at_first('E')
s1.display()
print("Total nodes in sll ->",s1.length())
s1.insert_at_first('F')
s1.display()
print("Total nodes in sll ->",s1.length())
s1.insert_at_loc('G',1)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.insert_at_loc('h',3)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.insert_at_loc('i',6)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.insert_at_loc('j',10)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.insert_at_loc('K',10)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_last()
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_first()
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_first()
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(1)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(3)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(5)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(5)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(4)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(3)
s1.display()
print("Total nodes in sll ->",s1.length())
s1.delete_at_loc(3)
s1.display()
print("Total nodes in sll ->",s1.length())
