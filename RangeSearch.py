class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p = self.get_insert_index(nums, target)
        if nums[p] != target:
            return -1, -1
        q = self.get_insert_index(nums, target - 1)
        if q < len(nums) - 1 and nums[q] != target:
            q = q + 1
        return q, p
    def get_insert_index(self, nums, target):
        lo, hi = 0, len(nums)
        mid = (lo + hi) // 2
        while mid != lo:
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
                return mid
            elif nums[mid] <= target:
                lo = mid
            else:
                hi = mid
            mid = (lo + hi) // 2
        return mid
        

s = Solution()
print(s.searchRange([2,4,5,6,6],6))