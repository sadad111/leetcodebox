class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        if len(prices) <= 4:
            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    ans += prices[i+1] - prices[i]

        buy1 = -2**31
        sale1 = 0
        buy2 = -2**31
        for i in prices:
            buy1 = max(buy1,-i)
            sale1 = max(sale1,i+buy1)
            buy2 = max(buy2,-i+sale1)
            ans = max(ans,i+buy2)
        return ans
