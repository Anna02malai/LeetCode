class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        local_min = prices[0]
        global_max = 0
        
        for i in prices:
            if i < local_min :
                local_min = i            

        l,r = 0, 1 #left = Buying, right = Selling
        max_pft = 0

        while r < len(prices):
            if prices[l] < prices[r] :
                pft = prices[r] - prices[l]
                max_pft = max(max_pft,pft)
            else:
                l = r
            
            r = r+1

        return max_pft
    
def main():
    ans = Solution()
    max_pft = ans.maxProfit([7, 1, 4, 2, 3, 6, 5])
    print(max_pft)

if __name__ == "__main__":
    main()
    