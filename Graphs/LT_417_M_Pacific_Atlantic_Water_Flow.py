class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r<0 or r == rows or c<0 or c==cols or heights[r][c] < prevHeight or (r,c) in visited):
                return

            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, pac, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][c])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res

def main():
    heights = [[1,2,2,3,5],
               [3,2,3,4,4],
               [2,4,5,3,1],
               [6,7,1,4,5],
               [5,1,1,2,4]]
    res = Solution()
    print(res.pacificAtlantic(heights))

if __name__ == "__main__":
    main()