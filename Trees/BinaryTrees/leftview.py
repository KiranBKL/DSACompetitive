class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
def LeftView(root):
    q=[]
    q.append(root)
    res=0
    while(len(q)):
        count,n=len(q),len(q)
        res=max(res,count)

        while(count!=0):
            
            temp=q.pop(0)
            if(count==n):
                print(temp.data)
            count-=1
            if(temp.left is not None):
                q.append(temp.left)
            if(temp.right is not None):
                q.append(temp.right)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right=Node(5)
root.left.right.right=Node(8)
root.left.right.left=Node(7)
root.right.left=Node(6)
root.right.left.left=Node(9)
root.right.left.right=Node(10)
LeftView(root)