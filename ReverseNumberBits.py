class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        print(n)
        print(int(str('{0:032b}'.format(n)[::-1]),2))
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        convertToString = str(format(x)[::-1])
        # print(convertToString)
        if convertToString[-1] == "-":
            if convertToString[0] == "0":
                newS = convertToString.strip("0")
                return int("-" + newS[:-1])
            else:
                ans =  int("-" + convertToString[:-1])
        else:
            ans = int(convertToString)
        if 2**-31 <= ans <= 2**31:
            return ans
        else:
            return 0
        
    
s = Solution()
# s.reverseBits(45)
print(s.reverse(-1000))