class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        profit = 0
        l = len(prices)
        while p2 < l:
            difference = prices[p2] - prices[p1]
            if difference < 1:
                p2 = p2 + 1
                p1 = p2 -1
            else:
                if profit < difference:
                    profit = difference
                p2 += 1
        return profit
            
        