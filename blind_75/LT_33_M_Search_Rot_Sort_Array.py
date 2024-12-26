class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1    

        while l <= r:            

            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            
            #Left Sorted Portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1
    
def main():
    nums = [1, 3]
    target = 3
    res = Solution()
    print(res.search(nums, target))

if __name__ == "__main__":
    main()