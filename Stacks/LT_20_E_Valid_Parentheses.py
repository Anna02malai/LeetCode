class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stk = []
        d = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in d:
                if stk and stk[-1] == d[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return True if not stk else False

def main():
    s = "([{}])"
    res = Solution()
    print(res.isValid(s))

if __name__ == "__main__":
    main()