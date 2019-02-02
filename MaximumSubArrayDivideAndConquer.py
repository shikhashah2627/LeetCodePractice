def partition(nums,left,right):
    if(left == right):
        return nums[left]
    mid_nums = (left + right)//2
    # print(mid_nums)
    sum1 = 0
    leftMax = -123456
    rightMax = -123456
    for i in range(mid_nums,left,-1):
        sum1 += nums[i]
        if(sum1 > leftMax):
            leftMax = sum1

    sum1 = 0  
    for i in range(mid_nums+1,right):
        sum1 += nums[i]
        if(sum1 > rightMax):
            rightMax = sum1
    print("left")
    print(left,mid_nums)
    print(partition(nums,left,mid_nums))
    print("right")
    print(right,mid_nums)
    print(partition(nums,mid_nums+1,right))
    print("max")
    print(max(partition(nums,left,mid_nums),partition(nums,mid_nums+1,right)))
    
    maxLeftRight = max(partition(nums,left,mid_nums),partition(nums,mid_nums+1,right))

    return max(maxLeftRight, leftMax + rightMax)
      
nums = [ 2, -4, 1, 9, -6, 7, -3]
print(partition(nums,0,len(nums)-1))