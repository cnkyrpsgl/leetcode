class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff_list=[0,0]
        for i in range (1, len(prices)):
            if prices[i]-prices[i-1]+diff_list[1]>=0:
                diff_list[1]=prices[i]-prices[i-1]+diff_list[1]
                diff_list[0]=max(diff_list[0],diff_list[1])
            else:
                diff_list[1]=0
        return diff_list[0]