class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []
        candidates.sort()

        def backtrack(i, curr, total):

            if total == target:
                res.append(curr[:])
                return

            if total > target or i >= len(candidates):
                return 
            
            #Include the Number
            curr.append(candidates[i])
            backtrack(i+1, curr, total + candidates[i])
            curr.pop()

            #Skip the Number
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr, total)
        
        backtrack(0, [], 0)
        return res

def main():
    candidates = [9,2,2,4,6,1,5]
    target = 8
    res = Solution()
    print(res.combinationSum2(candidates, target))

if __name__ == "__main__":
    main()