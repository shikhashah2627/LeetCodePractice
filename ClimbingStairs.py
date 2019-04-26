class Solution:
    def climbStairs(self, n):
        # #first method:
        # steps = [1,1]
        # for i in range(2,n+1):
        #     steps.append(steps[i-1] + steps[i-2])
        # return steps[n]
        #second method:
        return self.climb_stairs_recurse(0,n)
    def climb_stairs_recurse(self, i, n):
        if i > n:
            return 0
        if i == n:
            return i
        return self.climb_stairs_recurse(i+1,n) + self.climb_stairs_recurse(i+2,n)

s = Solution()
print(s.climbStairs(11))
        
        