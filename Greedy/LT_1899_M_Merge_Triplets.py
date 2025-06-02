class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
                
        return len(good) == 3

def main():
    triplets = [[1,2,3],[7,1,1]]
    target = [7,2,3]
    res = Solution()
    print(res.mergeTriplets(triplets, target))

if __name__ == "__main__":
    main()