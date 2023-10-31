class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        right = 1
        left = 0
        mxm = 0
        while right < len(prices):

            if prices[left] < prices[right]:
                
                mxm = max(mxm, prices[right] - prices[left])
            else:
                left = right
            right += 1
        
        return mxm
        