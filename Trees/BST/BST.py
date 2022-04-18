class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def search(root,key):
    if(root is None):
        return "No"
    if(root.data==key):
        return "Yes"
    elif(root.data<key):
        return search(root.right,key)
    return search(root.left,key)
def ceil(root,key):
    res=1000
    while(root!=None):
        if(key==root.data):
            return key.data
        elif(key>root.data):
            root=root.right
        else:
            res=min(root.data,res)
            root=root.right
    return res
def floor(root,key):
    res=None
    while(root!=None):
        if(key==root.data):
            return key.data
        elif(key<root.data):
            root=root.left
        else:
            res=root.data
            root=root.right
    return res
def findsuccessor(current_node):
    while current_node.left != None:
        current_node = current_node.left
    return current_node
def delete(current_node, data):
    if current_node == None:
        return current_node
    if data == current_node.data:        
        if current_node.left == None:
            current_node = current_node.right
        elif current_node.right == None:
            current_node = current_node.left
        else:
            current_node= findsuccessor(current_node)
            current_node.right = delete(current_node.right, current_node.data)
    elif data < current_node.data:
        current_node.left=delete(current_node.left, data)
    else:
        current_node.right=delete(current_node.right, data)
    return current_node
 

keys = [15, 10, 20, 8, 12, 16, 25]
root = None
for key in keys:
    root = insert(root, key)
#print(search(root,12))
#inorder(root)
#delete(root,12)
print(search(root,12))
print(ceil(root,14))
print(floor(root,14))
#print("\n")
#inorder(root)