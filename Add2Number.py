class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        part_list = nums[1:]
        for i in nums:
            for j in part_list:
                sum_init = i + j
                if(sum_init == target):
                    if (nums.index(i) == (part_list.index(j))):
                      final_output = [nums.index(i),(part_list.index(j)+4)] 
                    else:   
                        final_output = [nums.index(i),(part_list.index(j)+1)]                   
                    print (final_output)                        
                    return final_output

def main():
    list_num = Solution()
    list_of_num = [2,2,5,6,6,5,11]
    list_num.twoSum(list_of_num,10)

if __name__ == "__main__":
    main()           