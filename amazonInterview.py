# Important amazon questions
from collections import deque

def slidingMaximum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dq = deque()
    max_numbers = []

    for i in range(len(nums)):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k and dq and dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            max_numbers.append(nums[dq[0]])

    return max_numbers

# print(slidingMaximum([1,3,-1,-3,5,3,6,7],3))

def checkSubarraySum(nums, k):
    if k == 0:
        for i in range(0, len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        return False
    seen = {0, nums[0] % k}
    # print(seen)
    rs = nums[0]
    for i in range(1, len(nums)):
        rs = (rs + nums[i]) % k
        # print(rs)
        if rs in seen:
            return True
        seen.add(rs)
        # print(seen)
    return False

def lis(A):
        n=len(A)
        S=[1 for i in range(n)]
        for i in range(1,n):
            for j in range(0,i):
                if A[i]>A[j]:
                    #  checks whether that increases the possibility
                    if(S[j] + 1 > S[i]):
                        S[i] = S[j] + 1
            print(S)
        return max(S)
        
# print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

def numDecodings(self, A):
        n = len(A)
        count = [0] * (n+1)  
        count[0] = 1
        count[1] = 1
        if A[0] == '0': 
            return 0
        else:
            for i in range(2, n+1): 
                count[i] = 0
                if (A[i-1] > '0'): 
                    count[i] = count[i-1] 
                if (A[i-2] == '1' or (A[i-2] == '2' and A[i-1] < '7') ): 
                    count[i] += count[i-2] 
          
            return count[n]

def setZeroes(A):
    R = len(A)
    C = len(A[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if A[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                A[i][j] = 0
    return A
# print(setZeroes([[1,0,1],[1,1,1],[1,1,1]]))

def minCut(s):
        cut = [x for x in range(-1,len(s))]
        print(cut)
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]
# print(minCut('aab'))

def lengthOfLongestSubstring(A):
        n = len(A)
        S = [1] * n
        count = 0
        distanceCovered = []
        if len(A) == 1:
            return 1
        else: 
            for i in range(n):
                charSet = {}
                count = 0
                for j in range(i,n):
                    if A[j] not in charSet:
                        charSet[A[j]] = 1
                        count += 1
                    else:
                        distanceCovered.append(count)
                        count = 0
                        break
                distanceCovered.append(count)
        if len(distanceCovered) == 0:
            return len(A)
        else: return max(distanceCovered)
print(lengthOfLongestSubstring('dadbc'))