from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        adj = defaultdict(list)

        for i, p in enumerate(points):
            for j, pt in enumerate(points):
                if i!=j:
                    dist = abs(p[0] - pt[0]) + abs(p[1] - pt[1])
                    adj[i].append((dist, j))
        
        minH = [(0, 0)]
        visited = set()
        res_cost = 0

        while len(visited) < len(points):
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue

            visited.add(node)
            res_cost += cost

            for nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minH, nei)
        
        return res_costa

def main():
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
    res = Solution()
    print(res.minCostConnectPoints(points))

if __name__ == "__main__":
    main()