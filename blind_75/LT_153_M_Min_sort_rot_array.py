from math import ceil

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]
        l, r = 0, len(nums) - 1    

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            mid = (l + r)//2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid +1
            else:
                r = mid -1
     
        return res
    
def main():
    nums = [2, 1]
    res = Solution()
    print(res.findMin(nums))

if __name__ == "__main__":
    main()