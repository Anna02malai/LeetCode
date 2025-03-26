class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:

        meetings.sort()
        prev_end = 0

        for start, end in meetings:

            start = max(start, prev_end +1)
            length = end - start + 1
            days -= max(length, 0)
            prev_end = max(end, prev_end)
        
        return days

def main():
    days = 10
    meetings = [[5,7],[1,3],[9,10]]
    res = Solution()
    print(res.countDays(days, meetings))

if __name__ == "__main__":
    main()