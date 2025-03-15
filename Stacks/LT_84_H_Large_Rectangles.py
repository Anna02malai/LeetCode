class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stk = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx, height = stk.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stk.append([start, h])
        
        for i, h in stk:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

def main():
    heights = [2,1,5,6,2,3]
    res = Solution()
    print(res.largestRectangleArea(heights))

if __name__ == "__main__":
    main()