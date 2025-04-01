import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        self.stones = [int(-x) for x in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            x = heapq.heappop(self.stones)
            y = heapq.heappop(self.stones)

            if y > x:
                heapq.heappush(self.stones, x - y)
        
        if self.stones:
            return -1 * self.stones[0]
        else:
            return 0

def main():
    stones = [2,3,6,2,4]
    res = Solution()
    print(res.lastStoneWeight(stones))

if __name__ == "__main__":
    main()