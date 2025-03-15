class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []

        for i in tokens:
            if i == "+":
                stk.append(stk.pop() + stk.pop())
            elif i == "-":
                a, b = stk.pop(), stk.pop()
                stk.append(b-a)
            elif i == "*":
                stk.append(stk.pop() * stk.pop())
            elif i == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(float(b)/a))
            else:
                stk.append(int(i))
        
        return stk[0]

def main():
    inp = ["1","2","+","3","*","4","-"]
    res = Solution()
    print(res.evalRPN(inp))

if __name__ == "__main__":
    main()