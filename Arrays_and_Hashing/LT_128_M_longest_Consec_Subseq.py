class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet = set(nums)
        lng_subset = 0

        for n in nums:
            if n-1 not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                lng_subset = max(lng_subset, length)
        
        return lng_subset

def main():
    nums = [0, 1, 4, 5, 3, 2, 6]
    res = Solution()
    print(res.longestConsecutive(nums))

if __name__ == "__main__":
    main()