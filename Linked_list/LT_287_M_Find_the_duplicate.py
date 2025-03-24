class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2
        
def main():
    nums = [1,2,3,2,2]
    res = Solution()
    print(res.findDuplicate(nums))

if __name__ == "__main__":
    main()