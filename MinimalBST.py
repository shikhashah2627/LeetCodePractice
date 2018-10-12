#Definition for a binary search tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def createMinimalBST(self,array1, start, end):
        if (end < start):
            return
        mid = (start + end)/2 #index of mid value
        n = TreeNode(array1[mid])
        print(n.val)
        n.left = self.createMinimalBST(array1,start,mid-1)
        n.right = self.createMinimalBST(array1,mid+1,end)
        return n

def main():
    t1 = Solution()
    array_input = [1,2,3,4]
    t1.createMinimalBST(array_input,0,len(array_input)-1)
        

if __name__ == '__main__':
    main()    
