def sherlockAndAnagrams(s):
    d = {}
    for i in range(len(s)):
        subString = ''
        for j in range(i, len(s)):
            subString = ''.join(sorted(subString + s[j]))
            d[subString] = d.get(subString, 0) 
            d[subString] += 1
            
    print(d)
    anagramCount = 0
    nc = 0
    for k, v in d.items(): 
        nc += v
        # Aggregation
        anagramCount += (v*(v-1))//2
    return nc      

def countTriplets(arr, r):
    count = 0
    # with pair of 2 elements
    r2 = {}
    # with triples
    r3 = {}
    for k in arr:
        # probably completed triplet
        if k in r3:
            # this adds how many times the third element was encountered.
            count += r3[k]
        # second element
        if k in r2:
            if k*r in r3:
                r3[k*r] += r2[k]
            else:
                r3[k*r] = r2[k]
                    
        # first element
        if k*r in r2:
            r2[k*r] += 1
        else:
            r2[k*r] = 1
    return count

from collections import Counter
def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            cnt[ freq[value] ] -= 1
            freq[value] += 1
            cnt[ freq[value] ] += 1
        elif action == 2:
            if freq[value] > 0:
                cnt[ freq[value] ] -= 1
                freq[value] -= 1
                cnt[ freq[value] ] += 1
        else:
            result.append(1 if cnt[value] > 0 else 0)
    return result

def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        print(i)
        ia = sum(letter == chr(i) for letter in a)
        print("ia:",ia)
        ib = sum(letter == chr(i) for letter in b)
        print("ib:",ib)
        count += abs(ia-ib)
        print("count",count)
    return count
 
def isValid(s):
    s = list(s)
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]] += 1
        else: d[s[i]] = 1
    # print(d)
    newList = list(d.values())
    # print(newList)
    newList.sort()
    print(newList)
    getCount = max(newList.count(min(newList)),newList.count(max(newList)))
    maxValue = max(newList)
    minValue = min(newList)
    #  all frequencies are same  or remove one max-frequency or remove one min-frequency               
    if maxValue == minValue or (maxValue - minValue == 1 and getCount == len(newList)-1) or (minValue == 1 and newList.count(min(newList)) == 1 and getCount == len(newList)-1 )):
        return 'YES' 
    else: 
        return 'NO'   
s = 'aaabc'
print(isValid(s))
# sherlockAndAnagrams(s)
r = 5
arr = [1, 5, 5, 25, 125]
# print(countTriplets(arr,r))
queries = [[1, 3],[2, 3], [3, 2], [1, 4 ], [1, 5],  [3, 2], [2, 4], [3, 2]]
# print(freqQuery(queries))
# [1, 5], [1, 4],
# a = 'aabcdqqwerty'
# b = 'qwerty'
# print(makeAnagram(a, b))




