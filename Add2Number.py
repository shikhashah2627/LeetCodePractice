class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d =  {index_value: list_value for index_value, list_value in enumerate(nums)}
        print (d)
        final = []   
        x = 1         
        for i in d:
            j = i + 1
            for j in d:
                print i,j,i+j
                if(d[j] == (target - d[i])):
                    if(d[i]==d[j] and len(final) == 0):
                        if (len(nums) == 2 and (target == (d[i]+d[j]))):
                            final.append(i)
                            final.append(i+1)
                            return final
                        else:    
                            final.append(i)
                            x+=1
                            nums.remove(i)
                            print nums
                    #final.append(nums.index(j))
                    elif(i==j and len(final) > 0):
                        final.append(i+1)
                        return final 
                    else:
                        final.append(i)
                        final.append(j)
                        return final
        

             
        
def main():
    list_num = Solution()
    list_of_num = [1,3,4,2]
    x = list_num.twoSum(list_of_num,6)
    print (x)

if __name__ == "__main__":
    main()           