class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res= []
        def backtrack(i, curr, total):

            if total == target:
                res.append(curr[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return res

def main():
    nums = [2,5,6,9]
    target = 9
    res = Solution()
    print(res.combinationSum(nums, target))

if __name__ == "__main__":
    main()