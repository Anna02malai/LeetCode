class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        
        return res

def main():
    intervals = [[1,2],[2,4],[1,4]]
    res = Solution()
    print(res.eraseOverlapIntervals(intervals))

if __name__ == "__main__":
    main()