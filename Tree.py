class TREES:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

    def insert_the_ele(self,val):
        if self.data:
            if val<self.data:
                if self.left is None:
                    self.left=TREES(val)
                else:
                    self.left.insert_the_ele(val)
            elif val>self.data:
                if self.right is None:
                    self.right=TREES(val)
                else:
                    self.right.insert_the_ele(val)

    def display(self):
        if self.right:
            self.right.display()
        if self.left:
            self.left.display()
        print(self.data,end="->")



    def pre_order_traversal(self,root):
        if root:
            print(root.data,end=" - > ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
    

    def in_order_traversal(self,root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data,end=" - > ")
            self.in_order_traversal(root.right) 


    def post_order_traversal(self,root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data,end=" - > ") 


    def search_ele(self,val):
        if val < self.data:
            if self.left is None:
                return "value not found"
            else:
                return self.left.search_ele(val)
        elif val > self.data:
            if self.right is None:
                return "value not found"
            else:
                return self.right.search_ele(val)
        else:
            return "value found"



    def height_of_tree(self,root):
        if root is None:
            return 0
        leftheight = self.height_of_tree(root.left)
        rightheight = self.height_of_tree(root.right)
        maxheight = leftheight
        if rightheight > maxheight:
            maxheight = rightheight
        return maxheight + 1            



root= TREES(15)
root.insert_the_ele(20)
root.insert_the_ele(12)
root.insert_the_ele(8)
root.insert_the_ele(14)
root.insert_the_ele(6)
root.insert_the_ele(19)
root.insert_the_ele(10)
root.insert_the_ele(28)
root.display()
print()

print("Preorder Traversal:")
root.pre_order_traversal(root)
print()
print("Inorder Traversal:")
root.in_order_traversal(root)
print()
print("Postorder Traversal:")
root.post_order_traversal(root)
print()
print("Search Value:")
root.search_ele(19)
print("Height of Tree")
      
