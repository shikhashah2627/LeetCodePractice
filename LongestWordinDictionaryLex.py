# -*- coding: utf-8 -*-

class Solution:
    def findLongestWord(self, s, d):                        
        requriedWords = []
        for w in d:
            indices = []
            i, j = 0, 0         
            for i in range(len(s)):              
                if j < len(w):
                    if s[i] == w[j] :
#                        print(i,j)
                        indices.append(ord(w[j]))
                        j+=1
            if j == len(w):           
                requriedWords.append([w,indices])
        if len(requriedWords) == 0:
            return ""
        else:
            maxLength = 0
            maxLength = max(len(len1[1]) for len1 in requriedWords)
#            print(maxLength)
#            print(requriedWords)
            sameLengthWord = []
            for word in requriedWords:
                if len(word[1]) == maxLength:
                    sameLengthWord.append(word)
#            If only one word has the max length 
            if len(sameLengthWord) == 1:
                return sameLengthWord[0][0]
            else:
                temp = sameLengthWord[0][1]
                word = sameLengthWord[0][0]
                for i in range(1,len(sameLengthWord)):
                    
#                    Can be used when indec matters
#                    if requriedWords[i][1] < requriedWords[i+1][1]:
#                        return sameLengthWord[i][0]
#                    else:
#                        return sameLengthWord[i+1][0]
#                   Required to check lexicographically
                    if temp > sameLengthWord[i][1]:
                        word= sameLengthWord[i][0]
                        temp = sameLengthWord[i][1]
                    
                        
                return word
        

        
        
s = "wordgoodgoodgoodbestword"
d = ["word","good","best","good"]
s1 = Solution()
print(s1.findLongestWord(s,d))
        
        

        