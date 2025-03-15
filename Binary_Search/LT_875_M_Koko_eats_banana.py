import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            t = 0

            for p in piles:
                t += math.ceil(p/k)

            if t <= h:
                res = min(res, k)
                r = k -1
            else:
                l = k +1
        
        return res

def main():
    piles = [3,6,7,11]
    h = 8
    res = Solution()
    print(res.minEatingSpeed(piles, h))

if __name__ == "__main__":
    main()