class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)): 
            count += self.substring(s, i, i) 
            count += self.substring(s, i, i+1)
        
        return count
    
    def substring(self, st, l, r):
        res = 0
        while l>=0 and r<len(st) and st[l] == st[r]:
            res+=1
            l -= 1
            r += 1
        return res

def main():
    s = "aaa"
    res = Solution()
    print(res.countSubstrings(s))

if __name__ == "__main__":
    main()