class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r<0 or c<0 or r >= rows or c >= cols or (r, c) in path or word[i]!= board[r][c]):
                return False
            
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, r+1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

def main():
    board = [
            ["A","B","C","D"],
            ["S","A","A","T"],
            ["A","C","A","E"]
                    ]
    word = "CAT"
    res = Solution()
    print(res.exist(board, word))

if __name__ == "__main__":
    main()
