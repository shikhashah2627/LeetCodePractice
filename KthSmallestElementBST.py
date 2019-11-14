#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:12:28 2019

@author: shikhashah
"""

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#Note: 
#You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# Definition for a binary tree node. [230]
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    temp = []
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        print(self.temp)
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            self.temp.append(root.val)
            leftMin, rightMin = 0, 0
            leftMin = self.kthSmallest(root.left,k)
            return min(leftMin, rightMin)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
# assigning left and right
node3.left = node1
node3.right = node4
node1.right = node2
s = Solution()
print(s.kthSmallest(node3,2))
        