class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        res = []

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue 

            j, k = i+1, len(nums) -1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return res

def main():
    nums = [-1,0,1,2,-1,-4]
    res = Solution()
    print(res.threeSum(nums))

if __name__ == "__main__":
    main()