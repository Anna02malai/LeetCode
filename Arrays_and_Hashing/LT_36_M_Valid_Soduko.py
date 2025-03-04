from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        h_row = defaultdict(set)
        h_col = defaultdict(set)
        h_squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in h_row[r] or board[r][c] in h_col[c] or board[r][c] in h_squares[(r//3,c//3)]):
                    return False

                h_row[r].add(board[r][c])
                h_col[c].add(board[r][c])
                h_squares[(r//3,c//3)].add(board[r][c])

        # print(h_squares)

        return True   

def main():
    soduko =   [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
    
    res = Solution()
    print(res.isValidSudoku(soduko))

if __name__ == "__main__":
    main()