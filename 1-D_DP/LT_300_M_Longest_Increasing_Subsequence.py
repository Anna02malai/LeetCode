class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                
            
        return max(LIS)

def main():
    nums = [9,1,4,2,3,3,7]
    res = Solution()
    print(res.lengthOfLIS(nums))

if __name__ == "__main__":
    main()