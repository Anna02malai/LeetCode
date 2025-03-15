class Solution:
    def findMin(self, nums: list[int]) -> int:

        l, r = 0, len(nums) -1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1
        return res

def main():
    nums = [3,4,5,6,1,2]
    res = Solution()
    print(res.findMin(nums))

if __name__ == "__main__":
    main()