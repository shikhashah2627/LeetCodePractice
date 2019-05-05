# -*- coding: utf-8 -*-

# Definition for a binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

 

class Solution:
    def maxDepth(self, root):
        return self._count(root, 0)
        
    def _count(self, root, count):
        if root == None:
            return count
        leftHeight, rightHeight = 0, 0
        leftHeight += self._count(root.left, count + 1)
        rightHeight += self._count(root.right, count + 1)
#        print(leftHeight)
#        print(rightHeight)
        return max(leftHeight,rightHeight)
        

        
        
node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node3.right = node4
node4.right = node5
s = Solution()
print(s.maxDepth(node1))
        
        

        