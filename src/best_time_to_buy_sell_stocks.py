from typing import List

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# You can solve this problem using a simple greedy approach. 
# The idea is to buy the stock when the price is lower than the next day's price and 
# sell it immediately on that day. 

def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    max_profit = 0
    
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            max_profit += prices[i + 1] - prices[i]
    
    return max_profit


def test_max_profit():
    input = [7, 1, 5, 3, 6, 4]
    output = max_profit(input)
    print(f"Output: {output}")

    input2 = [1,2,3,4,5]
    output2 = max_profit(input2)
    print(f"Output: {output2}")

    input3 = [1,2,3,4,5]
    output3 = max_profit(input3)
    print(f"Output: {output3}")