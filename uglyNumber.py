import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [5, 3, 2]
        nums = [2, 3, 5]
        heapq.heapify(nums)
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums)
            for prime in primes:
                heapq.heappush(nums, p * prime)
                if p % prime == 0:
                    break
        return p
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i = j = k = 0
        count = 0
        
        while count < n:
            val = min(res[i]*2,min(res[j]*3,res[k]*5))
            if val == res[i]*2:
                i+=1
            if val == res[j]*3:
                j+=1
            if val == res[k]*5:
                k+=1
            count+=1
            if count == n:
                return res[-1]
            res.append(val)
            
    def nthSuperUglyNumber(self, n, primes):    
        nums = [1]
        heapq.heapify(nums)
        p = 1
        for i in range(n-1):
            # print(nums)
            p = heapq.heappop(nums)            
            for j in reversed(primes): 
                heapq.heappush(nums,p*j)
                if p%j == 0:
                    break
        return heapq.heappop(nums)
    
s = Solution()
print(s.nthUglyNumber(10))