# def palindrome(s):
#     s = list(s)
#     j = len(s) - 1
#     for i in range(len(s)):
#         if s[i] == s[j]:
#             j -= 1
#         elif i == 0 :
#             s.append(s[i])
#         elif i == len(s) // 2:
#             return s
#         else:
#             s.insert(i+1,s[j])
#             s.insert(j+2,s[i])
#             j -= 1
#             i += 2
#     return s    

# s1 = "abcdab"
# print(palindrome(s1))

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        count = 0
        temp = {}
        matched = []
        for match in list1:
            if match in list2:
                count += 1
                leastIndexSum = list1.index(match)+list2.index(match)
                if leastIndexSum in temp.keys():
                    matched.append(match)
                    temp[leastIndexSum] = matched
                else:
                    matched = []
                    matched.append(match)
                    temp[leastIndexSum] = matched
        finalOutput = temp[min(temp.keys())]
        if count == 0:
            return ""
        else:
            return finalOutput

        
s = Solution()
print(s.findRestaurant(
["dixyp","uq","q","KFC"],
["yl","fjugc","rlni","dixyp","uq","q","KFC"]))