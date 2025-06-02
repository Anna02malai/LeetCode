class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(size)
                size = 0
        
        return res

def main():
    s = "xyxxyzbzbbisl"
    res = Solution()
    print(res.partitionLabels(s))

if __name__ == "__main__":
    main()