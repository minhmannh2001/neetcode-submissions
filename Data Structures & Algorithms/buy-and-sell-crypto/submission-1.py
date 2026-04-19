class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # cập nhật giá mua thấp nhất
            if price < min_price:
                min_price = price
            else:
                # thử bán tại ngày hiện tại
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
