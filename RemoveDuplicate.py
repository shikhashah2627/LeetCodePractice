class Solution:
    def removeDuplicates(self, nums):
        # 159 cases get accepted
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         nums.remove(nums[i+1])
        #         return self.removeDuplicates(nums)
        #     else:
        #         continue
        # return len(nums)
        # Faster one
        Bool = True
        i = 1
        
        while Bool:
            if i < len(nums):
                if nums[i-1] == nums[i]:
                    nums.pop(i-1)
                else:
                    i += 1
            else:
                Bool = False
                
        return len(nums)
        
s = Solution()
print(s.removeDuplicates([1,1,2]))