class Solution:
    def rob(self, nums: list[int]) -> int:

        h1, h2 = 0, 0

        for n in nums:

            temp = max(n + h1, h2)
            h1 = h2
            h2 = temp
        
        return h2

def main():
    nums = [2,9,8,3,6]
    res = Solution()
    print(res.rob(nums))

if __name__ == "__main__":
    main()