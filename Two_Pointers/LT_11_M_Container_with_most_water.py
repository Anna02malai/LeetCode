class Solution:
    def maxArea(self, height: list[int]) -> int:

        l, r = 0, len(height) -1 
        res = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res

def main():
    height = [1,7,2,5,4,7,3,6]
    res = Solution()
    print(res.maxArea(height))

if __name__ == "__main__":
    main()