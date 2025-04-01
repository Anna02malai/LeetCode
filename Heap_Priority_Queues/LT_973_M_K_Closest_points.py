import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res

def main():
    points = [[0,2],[2,2]]
    k = 1
    res = Solution()
    print(res.kClosest(points, k))

if __name__ == "__main__":
    main()