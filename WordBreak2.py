class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        
        if dp[-1] == False:
            return []
        
        pos = []
        
        for i in range(len(dp)):
            if dp[i] == True:
                pos.append(i-1)
        pos.pop(0)
        res = []
        self.build(pos, s, "", res, wordDict, 0)
        return res
    
    def build(self, pos, s, choice, res, wordDict, start):
        if start > pos[-1]:
            res.append(choice[:-1])
            return 
        
        for i in range(len(pos)):
            if s[start: pos[i]+1] in wordDict:
                self.build(pos, s, choice+s[start:pos[i]+1]+" ", res, wordDict, pos[i]+1)
               
s = Solution()
print(s.wordBreak('catsanddogs',['cat', 'cats', 'and', 'sand', 'dog', 'dogs']))