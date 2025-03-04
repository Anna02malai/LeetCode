class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash_map = {}

        for i, value in enumerate(nums):
            if (target - value) in hash_map:
                return [hash_map[target - value], i]
            else:
                hash_map[value] = i
        
        return -1

lt_1 = Solution()
ans = lt_1.twoSum([2, 5, 1, 3], 4)
print(ans)