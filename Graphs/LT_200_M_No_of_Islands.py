from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in directions:
                    n_r, n_c = row + dr, col + dc
                    if (n_r in range(rows) and n_c in range(cols) and grid[n_r][n_c] == "1" and (n_r,n_c) not in visited):
                        visited.add((n_r,n_c))
                        q.append((n_r,n_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

def main():
    grid = [
            ["1","1","0","0","1"],
            ["1","1","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    res = Solution()
    print(res.numIslands(grid))

if __name__ == "__main__":
    main()