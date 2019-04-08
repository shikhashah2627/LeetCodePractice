# Given input will be list of list. 
# Output: Given a matrix of m x n elements (m rows, n columns), return all elements of 
            # the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix):
        Output = []
        InputLen = len(matrix)
        cmpMidCol = []
        if InputLen == 0:
            return Output
        elif InputLen == 1:
            Output += matrix[0]
            return Output
        else:
            Output += matrix[0]
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
            Output += lastCol
            lastRow = matrix[InputLen - 1]
            Output += lastRow[::-1] 
            Output += reversed(firstCol)
            return spiralOrder(self,cmpMidCol)
s1 = Solution()  
Input = [
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16],
]
print(s1.spiralOrder(Input))