class Node:
    def __init__(self,data):
        self.data = data 
        self.addr = None 

class Circular_Linked_List:
    def __init__(self):
        self.head = None 

    def insert_at_last(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            newNode.addr = newNode
        else:
            temp = self.head
            while temp.addr != self.head:
                temp = temp.addr
            temp.addr = newNode
            newNode.addr = self.head

    def display(self):
        if self.head is None:
            print("No nodes in CLL")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" -> ")
                temp = temp.addr
                if temp == self.head:
                    break
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
                    if temp == self.head:
                        break
                return count

    def insert_at_first(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            newNode.addr = newNode
        else:
            temp = self.head
            while temp.addr != self.head:
                temp = temp.addr
            temp.addr = newNode
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
            print("enter loc lessthan ->",self.length())
        else:
            temp = self.head
            cnt = 1
            while cnt < loc - 1:
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
            while temp.addr.addr != self.head:
                temp = temp.addr
            temp.addr = self.head

    def delete_at_first(self):
        if self.head is None:
            print("No nodes to remove")
        elif self.length() == 1:
            self.head = None 
        else:
            temp = self.head
            while temp.addr != self.head:
                temp = temp.addr
            temp.addr = self.head.addr
            self.head = self.head.addr 

cll = Circular_Linked_List()
cll.insert_at_last(10)
cll.insert_at_last(20)
cll.insert_at_last(30)
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.insert_at_first(40)
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.insert_at_first('A')
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.insert_at_loc(50,1)
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.insert_at_loc(60,3)
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.insert_at_loc(70,8)
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.insert_at_loc('C',8)
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.delete_at_last()
cll.display()
print("Total nodes on CLL ->",cll.length())
cll.delete_at_first()
cll.display()
print("Total nodes on CLL ->",cll.length())
