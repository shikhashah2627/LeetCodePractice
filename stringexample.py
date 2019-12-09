def wordSplit(s, wordDict):
    n = len(s)
    solutions = {}
    solutions[n] = ['']
    def solve(i):
        if i not in solutions:
            solutions[i] = [s[i:j] + (tail and (' ' + tail)) 
                            for j in range(i,n+1) 
                            if s[i:j] in wordDict 
                            for tail in solve(j)]
        return solutions[i]
    solve(0)
    return solutions[0]
    
def checkWordSplit(s, wordDict):
    n = len(s)
    possiblities = [False] * (n+1)
    possiblities[0] = True
    for i in range(1, n+1):
        for j in range(i-1,-1,-1):
            if possiblities[i] == True:
                break
            if possiblities[j]:
                if s[j:i] in wordDict:
                    possiblities[i] = True
    return possiblities[n] 
s = "shikhashah"
wordDict = set(["shikha", "sh", "a", "h"])
# print(wordSplit(s, wordDict))
print(checkWordSplit(s, wordDict))