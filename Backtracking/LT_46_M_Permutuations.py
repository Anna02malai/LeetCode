class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
            
        return res

def main():
    nums = [1, 2, 3]
    res = Solution()
    print(res.permute(nums))

if __name__ == "__main__":
    main()