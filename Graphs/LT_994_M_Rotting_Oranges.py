from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    
                    if (r not in range(rows) or c not in range(cols) or grid[r][c]!=1):
                        continue
                    grid[r][c] = 2
                    q.append([r,c])
                    fresh -= 1
            time += 1
        return time if fresh==0 else -1

def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    res = Solution()
    print(res.orangesRotting(grid))

if __name__ == "__main__":
    main() 