import heapq
def reorganizeString(S):
    # N = len(S)
    # A = []
    # s = set()
    # for x in S:
    #     s.add((S.count(x), x))
    # print(s)
    # # for c, x in sorted((S.count(x), x) for x in set(S)):
    # for c, x in sorted(s):
    #     print(c,x)
    #     if c > (N+1)/2: return ""
    #     A.extend(c * x)
    # ans = [None] * N
    # ans[::2], ans[1::2] = A[N//2:], A[:N//2]
    # return "".join(ans)
    pq = [(-S.count(x), x) for x in set(S)]
    heapq.heapify(pq)
    if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
        return ""

    ans = []
    while len(pq) >= 2:
        nct1, ch1 = heapq.heappop(pq)
        nct2, ch2 = heapq.heappop(pq)
        #This code turns out to be superfluous, but explains what is happening
        #if not ans or ch1 != ans[-1]:
        #    ans.extend([ch1, ch2])
        #else:
        #    ans.extend([ch2, ch1])
        ans.extend([ch1, ch2])
        if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
        if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

    return "".join(ans) + (pq[0][1] if pq else '')
print(reorganizeString('aaabbbbccswr'))
#############
# def isPossible(Str): 
  
#     # To store the frequency of 
#     # each of the character 
#     freq = dict() 
  
#     # To store the maximum frequency so far 
#     max_freq = 0
#     for j in range(len(Str)): 
#         freq[Str[j]] = freq.get(Str[j], 0) + 1
#         if (freq[Str[j]] > max_freq): 
#             max_freq = freq[Str[j]] 
  
#     # If possible 
#     if (max_freq <= (len(Str) - max_freq + 1)): 
#         return True
#     return False
  
# # Driver code 
# Str = "geeksforgeeks"
  
# if (isPossible(Str)): 
#     print("Yes") 
# else: 
#     print("No") 