class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        l, r = 0, 0
        substring = set()

        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                r += 1
            
            else:
                substring.remove(s[l])
                l += 1
            res = max(res, r-l)    
        return res
    
def main():
    s = "pwwkew"
    res = Solution()
    print(res.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()