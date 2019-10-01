class Node(object): 
      
    """Binary tree Node class has  
    data, left and right child"""
    def __init__(self, item): 
        self.data = item 
        self.left = None
        self.right = None
  
def BTToDLLUtil(root): 
      
    """This is a utility function to  
    convert the binary tree to doubly  
    linked list. Most of the core task 
    is done by this function."""
    if root is None: 
        return root 
  
    # Convert left subtree  
    # and link to root 
    if root.left: 
          
        # Convert the left subtree 
        left = BTToDLLUtil(root.left) 
  
        # Find inorder predecessor, After  
        # this loop, left will point to the  
        # inorder predecessor of root 
        while left.right: 
            left = left.right 
  
        # Make root as next of predecessor 
        left.right = root 
          
        # Make predecessor as  
        # previous of root 
        root.left = left 
  
    # Convert the right subtree 
    # and link to root 
    if root.right: 
          
        # Convert the right subtree 
        right = BTToDLLUtil(root.right) 
  
        # Find inorder successor, After  
        # this loop, right will point to  
        # the inorder successor of root 
        while right.left: 
            right = right.left 
  
        # Make root as previous  
        # of successor 
        right.left = root 
          
        # Make successor as  
        # next of root 
        root.right = right 
  
    return root 
  
def BTToDLL(root): 
    if root is None: 
        return root 
  
    # Convert to doubly linked  
    # list using BLLToDLLUtil 
    root = BTToDLLUtil(root) 
      
    # We need pointer to left most  
    # node which is head of the  
    # constructed Doubly Linked list 
    while root.left: 
        root = root.left 
  
    return root 
  
def print_list(head): 
      
    """Function to print the given 
       doubly linked list"""
    if head is None: 
        return
    while head: 
        print(head.data, end = " ") 
        head = head.right 
  
# Driver Code 
if __name__ == '__main__': 
    root = Node(10) 
    root.left = Node(12) 
    root.right = Node(15) 
    root.left.left = Node(25) 
    root.left.right = Node(30) 
    root.right.left = Node(36) 
  
    head = BTToDLL(root) 
    print_list(head) 