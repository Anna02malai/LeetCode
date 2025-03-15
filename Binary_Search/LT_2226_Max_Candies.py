class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        total = sum(candies)
        if total <= k:
            return 0
        l, r = 1, total//k
        res = 0

        while l <= r:
            mid = (l+r)//2
            count = 0

            for c in candies:
                if c >= mid:
                    count += c//mid
                if count >=k:
                    break
            
            if count >= k:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res

def main():
    candies = [5,8,6]
    k = 3
    res = Solution()
    print(res.maximumCandies(candies, k))

if __name__ == "__main__":
    main()