# Given input will be list of list. 
# Output: Given a matrix of m x n elements (m rows, n columns), return all elements of 
            # the matrix in spiral order.

class Solution:
    Output = []
    # def __init__(self, Output):
    #     self.Output = []
    def spiralOrder(self, matrix):
        InputLen = len(matrix)
        cmpMidCol = []
        if InputLen == 0:
            return self.Output
        elif InputLen == 1:
            self.Output += matrix[0]
            FinalOutput = self.Output
            self.Output = []
            return FinalOutput
        else:
            self.Output = []
            self.Output += matrix[0]
            lastCol = []
            firstCol = []
            
            for row in range(1,InputLen-1):
                midCol = []
                for col in range(0,len(matrix[row])):
                    if col == len(matrix[row]) - 1:
                        lastCol.append(matrix[row][col])
                    elif col == 0:
                        firstCol.append(matrix[row][col])
                    else:
                        midCol.append(matrix[row][col])
                cmpMidCol.append(midCol)
            self.Output += lastCol
            lastRow = matrix[InputLen - 1]
            self.Output += lastRow[::-1] 
            self.Output += reversed(firstCol)
            if len(cmpMidCol) >= 1:
                return self.spiralOrder(cmpMidCol)
            else:
                FinalOutput = self.Output
                self.Output = []
                return FinalOutput

Input1 = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8],
 [ 9, 10, 11, 12],
]
Input2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Input3 = [[2,3]]
Input4 = [[1]]
s1 = Solution()  
s1.spiralOrder(Input1)
s1.spiralOrder(Input2)
print(s1.spiralOrder(Input4))
print(s1.spiralOrder(Input3))
