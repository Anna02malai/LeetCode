class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            
            if n == 0:
                currMax, currMin = 1, 1
                continue
            
            tmp = n * currMax
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            
            res = max(res, currMax)            

        return res

def main():
    nums = [2, 3, -1, 4]
    res = Solution()
    print(res.maxSubArray(nums))

if __name__ == "__main__":
    main()       





