class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1
        
        for c in t:
            if t_dict[c] != s_dict[c]:
                return False
        return True

def main():
    s = "racecar"
    t = "carrace"
    res = Solution()
    print(res.isAnagram(s,t))

if __name__ == "__main__":
    main()