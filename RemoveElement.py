class Solution:
    def removeElement(self, nums, val):
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums.remove(nums[i])
                return self.removeElement(nums,val)
            else:
                continue
                
        return len(nums)
        
s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))