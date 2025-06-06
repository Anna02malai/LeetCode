class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part[::])
                return 
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
    
    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True

def main():
    s = "aab"
    res = Solution()
    print(res.partition(s))

if __name__ == "__main__":
    main()