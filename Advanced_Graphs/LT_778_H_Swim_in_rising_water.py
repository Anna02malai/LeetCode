import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minH = [(grid[0][0], 0, 0)]
        visited = set()
        t = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minH:
            time, r, c = heapq.heappop(minH)

            if r == rows -1 and c == cols -1:
                return max(t, time)

            visited.add((r, c))
            t = max(t, time)

            for dr, dc in directions:
                row, col = dr +r, dc +c
                if row >= 0 and col>= 0 and row < rows and col < cols and (row, col) not in visited:
                    heapq.heappush(minH, (grid[row][col], row, col))
        
def main():
    grid = [
            [0,1,2,10],
            [9,14,4,13],
            [12,3,8,15],
            [11,5,7,6]]
    res = Solution()
    print(res.swimInWater(grid))

if __name__ == "__main__":
    main()