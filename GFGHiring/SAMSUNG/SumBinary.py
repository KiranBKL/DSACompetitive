
class Solution:
    def toSumTree(self, Node) : 
          
        # Base case  
        if(Node == None) : 
            return 0
      
        # Store the old value  
        old_val = Node.data  
      
        # Recursively call for left and  
        # right subtrees and store the sum as  
        # new value of this node  
        Node.data = self.toSumTree(Node.left) +  self.toSumTree(Node.right)  
      
        # Return the sum of values of nodes  
        # in left and right subtrees and  
        # old_value of this node  
        return Node.data + old_val  