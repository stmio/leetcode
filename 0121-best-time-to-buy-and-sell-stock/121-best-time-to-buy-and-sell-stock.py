class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices[1:]:
            s = max(0, i - buy)

            if s > profit:
                profit = s

            if i < buy:
                buy = i
            
        return profit