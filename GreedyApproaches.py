def luckBalance(k, contests):
    luckBalanceCalc = 0
    importantList = []
    for i in range(len(contest)):
        if contest[i][1] == 0:
            luckBalanceCalc += contest[i][0]
        else: importantList.append(contest[i][0])
    importantList.sort()
    importantList = importantList[::-1]
    luckBalanceCalc += sum(importantList[:k])
    luckBalanceCalc -= sum(importantList[k:])
    return luckBalanceCalc
    
    # heap = []
    # heapq.heapify(heap)
    # luck = 0
    # for L,T in contests:
    #     if not T:
    #         luck = luck + L
    #     elif k < 1:
    #         luck = luck - L
    #     elif len(heap) < k:
    #         heapq.heappush(heap, L)
    #     else:
    #         luck = luck - heapq.heappushpop(heap, L)
    # return luck + sum(heap)
def getMinimumCost(k, c):
    c.sort(reverse=True)
    print(c)
    l=len(c)
    t=0
    for i in range(l):
        print(t+(int(i/k)+1)*c[i])
        t=t+(int(i/k)+1)*c[i]
    return t

def frequency(s):
    res = defaultdict(int)
    for char in s:
        res[char] += 1
    return res

def reverseShuffleMerge(s):
    char_freq = frequency(s)
    used_chars = defaultdict(int)
    remain_chars = dict(char_freq)
    res = []
    
    def can_use(char):
        return (char_freq[char] // 2 - used_chars[char]) > 0
    
    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
    for char in reversed(s):
        if can_use(char):
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] -= 1
            
            used_chars[char] += 1
            res.append(char)
        
        remain_chars[char] -= 1
    
    return "".join(res)
        
contest=[[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
k = 3
# print(luckBalance(k,contest))
print(getMinimumCost(2, [2, 5, 6]))