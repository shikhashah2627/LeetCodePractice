# s = '12345'
# s = '99910001001'
# DeepLearning.io interview question
def isSequence(s):
    if not s:
        return []
    cutSize = 1
    finalList = []
    while cutSize <= len(s):
        tempList = [0]
        i = 0
        tempCut = cutSize
        while i < len(s):
            temp = int(''.join(s[i:i+tempCut]))
            if temp - tempList[-1] == 1 or len(tempList) == 1:
                tempList.append(temp)
            if (temp%9 == 0 and len(str(temp)) == tempCut) or temp == 9: 
                tempCut += 1
                i += len(str(temp))
            else:
                i += tempCut
        cutSize += 1
        if len(tempList) > 2:
            print(tempList)
            finalList.append(tempList[1:])
        # return max(finalList)
isSequence('9899100')