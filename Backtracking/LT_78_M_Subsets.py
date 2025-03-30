class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):

            if i == n:
                res.append(sol[:])
                return

            #Do not include i
            backtrack(i+1)

            #Include i
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res

def main():
    nums = [1,2,3]
    res = Solution()
    print(res.subsets(nums))

if __name__ == "__main__":
    main()