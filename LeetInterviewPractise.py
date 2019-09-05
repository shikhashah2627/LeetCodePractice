# 523, 560, 713
def checkSubarraySum(nums, k):
    if k == 0:
        return any( nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
    reminder = 0
    cache = {0:-1}
    for i in range(len(nums)):
        reminder = (reminder + nums[i]) % k
        if reminder in cache and i - cache[reminder] > 1:
            return True
        if reminder not in cache:
            cache[reminder] = i
    return False

# print(checkSubarraySum([23, 4, 5, 6, 7, 8], 18))   

def subarraysum(nums, k):
    cache = {0:1}
    sum, count = 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in cache:
            count += cache[sum-k]
        if sum in cache:
            cache[sum] = cache[sum]+1
        else:
            cache[sum] = 1
    # print(cache)
    return count
    
# print(subarraysum([3, 4, 7, 2, -3, 1, 4, 2], 7))

def numSubarrayProductLessThanK(nums, k):
    if k <= 1: return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
print(numSubarrayProductLessThanK([10, 5, 2, 3], 20))       