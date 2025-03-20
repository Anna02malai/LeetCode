from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        l, r = 0, 0
        res = []
        q = deque()

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res

def main():
    nums = [1,2,1,0,4,2,6]
    k = 3
    res = Solution()
    print(res.maxSlidingWindow(nums, k))

if __name__ == "__main__":
    main()

