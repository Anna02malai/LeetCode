class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
        
        return maxSub

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution()
    print(res.maxSubArray(nums))

if __name__ == "__main__":
    main()