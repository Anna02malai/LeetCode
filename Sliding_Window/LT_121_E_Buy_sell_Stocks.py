class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy, sell = float("inf"), 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                buy = prices[r]
                l = r
                r += 1
            else:
                sell = max(sell, prices[r] - prices[l])
                r += 1
        return sell

def main():
    prices = [10,1,5,6,7,1]
    res = Solution()
    print(res.maxProfit(prices))

if __name__ == "__main__":
    main()
