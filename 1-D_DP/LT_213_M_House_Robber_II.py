class Solution:
    def rob(self, nums: list[int]) -> int:
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])
    
    def helper(self, houses):
        h1, h2 = 0, 0
        for n in houses:
            tmp = max(h1 +n, h2)
            h1 = h2
            h2 = tmp
        return h2

def main():
    nums = [2,9,8,3,6]
    res = Solution()
    print(res.rob(nums))

if __name__ == "__main__":
    main()