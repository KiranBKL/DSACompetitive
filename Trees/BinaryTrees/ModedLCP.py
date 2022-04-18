class Node:
    i=0
    maxval=0
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
    def LCP(self,root):
        if(root==None):
            return [0,0]
        inc,dec=1,1
        if(root.left):
            l=self.LCP(root.left)
            if(root.data==root.left.data+1):
                dec=l[1]+1
            elif(root.data==root.data-1):
                inc=l[0]+1
        if(root.right):
            r=self.LCP(root.right)
            if(root.data==root.right.data+1):
                dec=max(dec,r[1]+1)   
            elif(root.data==root.right.data-1):
                inc=max(inc,r[0]+1)
        self.maxval=max(self.maxval,dec+inc-1)
        return [inc,dec]
root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(3)
root.left.right=Node(1)
root.right.right=Node(5)
root.right.right.right=Node(6)
root.LCP(root)
print(root.maxval)