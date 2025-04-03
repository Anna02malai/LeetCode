import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return minHeap[0]

def main():
    nums = [2,3,1,5,4]
    k = 2
    res = Solution()
    print(res.findKthLargest(nums, k))

if __name__ == "__main__":
    main()

