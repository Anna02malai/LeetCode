class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        a = set(nums)
        
        if len(a) == len(nums):
            return False
        
        return True
        

def main():
    nums = [1, 2, 3, 4, 5]
    result = Solution()
    print(result.containsDuplicate(nums))

if __name__ == "__main__":
    main()