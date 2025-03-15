class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        stk = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stk))
                return 
            
            if openN < n:
                stk.append("(")
                backtrack(openN+1, closedN)
                stk.pop()
            
            if closedN < openN:
                stk.append(")")
                backtrack(openN, closedN+1)
                stk.pop()
        backtrack(0, 0)
        return res

def main():
    n = 3
    res = Solution()
    print(res.generateParenthesis(n))

if __name__ == "__main__":
    main()