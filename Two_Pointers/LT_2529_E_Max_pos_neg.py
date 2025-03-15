class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def lower_bound(nums):
            l, r = 0, len(nums) - 1
            i = len(nums)

            while l <= r:
                mid = (l+r)//2
                if nums[mid] < 0:
                    l += 1
                else:
                    r -= 1
                    i = mid
            
            return i
        
        def upper_bound(nums):
            l, r = 0, len(nums) - 1
            i = len(nums)

            while l <= r:
                mid = (l+r)//2
                if nums[mid] <= 0:
                    l += 1
                else:
                    r -= 1
                    i = mid
            
            return i
        
        pos = len(nums) - upper_bound(nums)
        neg = lower_bound(nums)
        return max(pos, neg)

def main():
    nums = [-3,-2,-1,0,0,1,2]
    res = Solution()
    print(res.maximumCount(nums))

if __name__ == "__main__":
    main()
    