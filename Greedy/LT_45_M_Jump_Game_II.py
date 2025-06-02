class Solution:
    def jump(self, nums: list[int]) -> int:

        res = 0
        l = r = 0

        while r < len(nums) -1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest 
            res += 1
        
        return res

def main():
    nums = [2,4,1,1,1,1]
    res = Solution()
    print(res.jump(nums))

if __name__ == "__main__":
    main()