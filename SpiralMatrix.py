## def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    Output = []
    def spiralOrder(self, matrix):
        FinalOutput = []
        try:
            InputLen = len(matrix)
            cmpMidCol = []
            if InputLen == 0:
                FinalOutput = self.Output
                self.Output = None
                return FinalOutput
            elif InputLen == 1:
                self.Output += matrix[0]
                FinalOutput = self.Output
                self.Output = None
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
                    self.Output = None
                    return FinalOutput
        finally:
            self.Output = None
