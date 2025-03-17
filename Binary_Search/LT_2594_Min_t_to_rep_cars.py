import math

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        
        l, r = 1, ranks[0] * pow(cars, 2)
        res = float("inf")

        while l <= r:
            m = (l+r)//2
            count = 0
            for mech in ranks:
                count += math.floor(math.sqrt(m/mech))
                if count >= cars:
                    break
            
            if count >= cars:
                res = min(res, m)
                r = m -1
            
            else:
                l = m + 1
        return res

def main():
    ranks = [4,2,3,1]
    cars = 10
    res = Solution()
    print(res.repairCars(ranks, cars))

if __name__ == "__main__":
    main()