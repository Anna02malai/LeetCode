from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        visited = set()
        total = 0
        minH = [(0, k)]

        while minH:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue

            visited.add(node)
            total = max(total, cost)

            for nei, wt in edges[node]:
                if nei not in visited:
                    heapq.heappush(minH, (total + wt, nei))
        
        return total if len(visited) == n else -1

def main():
    times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
    n = 4
    k = 1
    res = Solution()
    print(res.networkDelayTime(times, n, k))

if __name__ == "__main__":
    main()