class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == n:
                res.append(subset[:])
                return
            
            #Include the number we are currently in
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            #Do not include the number we are currently in and skip duplicates
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res

def main():
    nums = [1, 2, 2]
    res = Solution()
    print(res.subsetsWithDup(nums))

if __name__ == "__main__":
    main()