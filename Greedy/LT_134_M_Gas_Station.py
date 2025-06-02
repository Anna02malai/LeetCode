class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
            
        return res

def main():
    gas = [1,2,3,4]
    cost = [2,2,4,1]   
    res = Solution()
    print(res.canCompleteCircuit(gas, cost))

if __name__ == "__main__":
    main()