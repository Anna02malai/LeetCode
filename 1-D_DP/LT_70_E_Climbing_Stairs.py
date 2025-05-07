class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one

def main():
    n = 5
    res = Solution()
    print(res.climbStairs(n))

if __name__ == "__main__":
    main()