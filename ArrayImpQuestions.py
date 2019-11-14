def countTriplets(nums):
    # nums.sort() 
    n = len(nums)
    # count = 0
    # for i in range(0, n-2):
    #     j = i+1
    #     while j < n:
    #         if nums[i] + nums[j] in nums:
    #             count += 1
    #         j += 1
    # return count
    max_val = 0
    for i in range(n):  
        max_val = max(max_val, nums[i]) 
  
    freq = [0 for i in range(max_val + 1)]  
  
    for i in range(n):  
        freq[nums[i]] += 1
  
    ans = 0 # stores the number of ways
    for i in range(1, max_val + 1):  
        for j in range(i + 1, max_val - i + 1):  
            ans += freq[i] * freq[j] * freq[i + j]  
  
    return ans  
        
    
# print(countTriplets([1,3,4,5]))
import heapq
def mergeTwoArrays(n1,n2):
    heapq.heapify(n2)
    for i in n1:
        heapq.heappush(n2,i)
    print(n2)
# mergeTwoArrays([1,4,6,7,8,9],[2,3,4,5])

# Equilibrium index of an array
def Equilibrium(nums):
    n,i,j = len(nums),0,len(nums)-1
    sum1 = sum2 = ans = 0
    while i < n and j > 0:
        if (sum1+nums[i] == sum2 + nums[j]):
            ans = i+j-1
            break
        sum1+=nums[i]
        sum2+=nums[j]
        i+=1
        j-=1
    return ans    
# print(Equilibrium([-7, 1, 2,3,-8,-9]))


# Python program to find 
# maximum amount of water that can 
# be trapped within given set of bars. 
# Space Complexity : O(1) 
  
def findWater(arr,n): 
  
    # initialize output 
    result = 0
       
    # maximum element on left and right 
    left_max = 0
    right_max = 0
       
    # indices to traverse the array 
    lo = 0
    hi = n-1
       
    while(lo <= hi):  
      
        if(arr[lo] < arr[hi]): 
          
            if(arr[lo] > left_max): 
  
                # update max in left 
                left_max = arr[lo] 
            else: 
  
                # water on curr element = max - curr 
                result += left_max - arr[lo] 
            lo+=1
          
        else: 
          
            if(arr[hi] > right_max): 
                # update right maximum 
                right_max = arr[hi] 
            else: 
                result += right_max - arr[hi] 
            hi-=1
          
    return result 
   
# Driver program 
  
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
n = len(arr) 
  
# print("Maximum water that can be accumulated is ", 
        # findWater(arr, n)) 
        
def sellBuyStock(stocks):
    j = 0 
    c = 0
    for i in range(1,n):
        if li[i-1]>li[i] :
            if i-j>1:
                print("(",end="")
                print(j ,i-1,end="")
                print(")",end=" ")
                c = 1
                j = i
            else:
                j+=1
                
        elif (i==(n-1) and li[i]>li[j] and i>j):
            print("(",end="")
            print(j, i,end="")
            print(")",end="")
            c = 1
    if c == 0 :
        print("No Profit")
    else:
        print()

    t-=1

def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    # def mycmp(a, b):
    #     x = a + b
    #     y = b + a
    #     return (x > y) - (x < y)
                
    # return str(int("".join(sorted([str(i) for i in nums], reverse=True, key=mycmp))))
    nums = sorted([str(n) for n in nums],key = lambda x:x*(32),reverse=True)
    return "0" if set(nums) == set("0") else "".join(nums)
    
print(largestNumber([3,35,50,55,9]))
    
    
    