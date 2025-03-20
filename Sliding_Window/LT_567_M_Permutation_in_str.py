class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        d1, d2 = [0]*26, [0]*26
        matches = 0

        for i in range(len(s1)):
            d1[ord(s1[i]) - ord("a")] += 1
            d2[ord(s2[i]) - ord("a")] += 1
        
        for i in range(26):
            if d1[i] == d2[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord("a")
            d2[idx] += 1
            if d2[idx] == d1[idx]:
                matches += 1
            elif d1[idx] + 1 == d2[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord("a")
            d2[idx] -= 1
            if d2[idx] == d1[idx]:
                matches += 1
            elif d1[idx] - 1 == d2[idx]:
                matches -= 1   

            l += 1
        return matches == 26

def main():
    s1 = "abc"
    s2 = "lecaabee"
    res = Solution()
    print(res.checkInclusion(s1, s2))

if __name__ == "__main__":
    main()        
