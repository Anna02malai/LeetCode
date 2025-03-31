class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        colset = set()
        pos_diag = set()
        neg_diag = set()

        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in colset or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                    
                colset.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                colset.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return res

def main():
    n = 4
    res = Solution()
    print(res.solveNQueens(n))

if __name__ == "__main__":
    main()
