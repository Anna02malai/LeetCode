class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
    
def main():
    s = "neetcode"
    wordDict = ["neet","code"]
    res = Solution()
    print(res.wordBreak(s, wordDict))

if __name__ == "__main__":
    main()