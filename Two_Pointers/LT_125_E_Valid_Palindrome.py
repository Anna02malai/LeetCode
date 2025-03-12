class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l, r = 0, len(s) -1
        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

def main():
    s = "Madam, in Eden, I'm Adam"
    res = Solution()
    print(res.isPalindrome(s))

if __name__ == "__main__":
    main()