from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = defaultdict(list)
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != ".":
                    if val in res[3 * (i // 3) + j // 3 + 20] or val in res[i + 10] or val in res[j]:
                        return False
                    res[3 * (i // 3) + j // 3 + 20].append(val) #for every box check
                    res[i + 10].append(val) # for every row check
                    res[j].append(val) #for every column check
        return True
        
s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["5",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]))