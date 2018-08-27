class Node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=self.right=None
    def insert(self,node):
        if node.start>=self.end:
            if not self.right:
                self.right=node
                return True
            else:
                return self.right.insert(node)
        elif node.end<=self.start:
            if not self.left:
                self.left=node
                return True
            else:
                return self.left.insert(node)
        else:
            return False
class MyCalender:
    def __init(self):
        self.root=None
    def book(self, start, end):
        if self.root==None:
            self.root=Node(start,end)
            return True
        else:
            return self.root.insert(Node(start,end))

obj=MyCalender()



        