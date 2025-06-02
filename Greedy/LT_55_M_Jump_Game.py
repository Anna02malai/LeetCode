class Solution:
    def jump(self, nums: list[int]) -> int:
        goal = len(nums) -1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal == 0 else False

def main():
    nums = [2,4,1,1,1,1]
    res = Solution()
    print(res.jump(nums))

if __name__ == "__main__":
    main()