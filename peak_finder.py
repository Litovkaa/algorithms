# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        min_cost, max_profit = float("inf"), float("-inf")
        for p in prices:
            if p < min_cost:
                min_cost = p
            if p - min_cost > max_profit:
                max_profit = p - min_cost

        return max_profit


if __name__ == "__main__":
    print(Solution.max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
