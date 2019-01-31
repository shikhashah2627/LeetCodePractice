'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import sys
class Solution:
    def maxSubArray_bruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -sys.maxsize -1
        sum1 = 0
        for i in range(0,len(nums)):
            sum1 = 0
            for j in range(i,len(nums)):
                sum1 += nums[j]
                if(sum1 > maxSum):
                    maxSum = sum1
        return maxSum
    def maxSubArray_divideAndConquer(self, nums):
        mid = nums
    
    def partitioned_word(self,left,right):
        
s = Solution()
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray_bruteForce([1,2,-1,-2,2,1,-2,1,4,-5,4]))
        