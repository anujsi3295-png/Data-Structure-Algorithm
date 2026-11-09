class STACK:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.s1 = []

    def push(self,val):
        if len(self.s1) > 0 and len(self.s1[-1]) < self.maxSize:
            self.s1[-1].append(val)
        else:
            self.s1.append([val])

    def display(self):
        print(self.s1)

    def pop(self):
        if len(self.s1) == 0:
            print("stack is empty")
        else:
            if len(self.s1[-1]) > 1:
                self.s1[-1].pop()
            else:
                self.s1.pop()

    def popAT(self,st_num):
        if st_num <= len(self.s1):
            self.s1[st_num-1].pop() 
        else:
            print("stack num dosen't exists")


st = STACK(4)
st.push('JS')
st.push('C#')
st.push('C++')
st.push('objective C')
st.push('CS')
st.push('groovy')
st.push('DSA')
st.push('Sql')
st.push('ReactJs')
st.push('J2ee')
st.push("ADV java")
st.push('html')
st.push("Kotlin")
st.push('jdbc')
st.display()
print()
# st.pop()
# st.pop()
# st.pop()
st.popAT(2)
st.popAT(1)
st.popAT(3)
st.popAT(4)
st.popAT(45)
st.display()