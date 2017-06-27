class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        if k > len(prices)/2:
            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    ans += prices[i+1] - prices[i]

        for i in range(1,k):
            tmpMax =  -prices[0]
            for j in range(1,len(prices)):
                t[i][j] = max(t[i][j - 1], prices[j] + tmpMax)
                tmpMax = max(tmpMax, t[i - 1][j - 1] - prices[j])

        return t[k][len - 1];
