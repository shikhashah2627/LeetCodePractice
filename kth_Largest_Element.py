class Solution:
    def findKthLargest(self, nums, k):
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        sortedArray = sorted(d.items(), reverse = True, key=lambda d:d[0])
        print(sortedArray)
        count = 1
        for key, value in sortedArray:
            if len(sortedArray) == 1 and k <= value:
                return key
            else:
                if k == count:
                    return key
                count += value
                if count > k:
                    return key

s1 = Solution()
print(s1.findKthLargest([3,3,3,3,4,3,3,3,3],9))