class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        buy_day = -1
        sell_day = -1

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                    buy_day = i
                    sell_day = j

        return max_profit
