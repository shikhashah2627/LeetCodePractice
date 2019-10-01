def lengthOfLIS(nums) -> int:
    if not nums:
        return 0
    # dp = [1 for x in range(len(nums))]
    # for i in range(len(nums)):
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # return max(dp)
    n = len(nums)
    LIS = [None] * n
    size = 0 
    for i in range(n):
        low, high = 0, size
        while low < high:
            mid = low + (high - low)//2
            if LIS[mid] < nums[i]:
                low = mid + 1
            else:
                high = mid
        LIS[low] = nums[i]
        if low == size:
            size += 1          
    return size
        
print(lengthOfLIS([10,9,2,5,3,7,101,18]))