# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(cost):
            if cost[1:]:
                return cost[0] + min([dp(cost[1:]), dp(cost[2:])])

            return cost[0] if cost else 0

        return min([dp(cost), dp(cost[1:])])

    def min_cost_climbing(self, cost: List[int]) -> int:
        c = 0
        i = 0
        cost_rev = cost[::-1]
        while i <= len(cost) - 2:
            if cost_rev[i] < cost_rev[i + 1]:
                print("One step:", cost_rev[i])
                c += cost_rev[i]
                i += 1
            else:
                print("Two steps: ", cost_rev[i+1])
                c += cost_rev[i + 1]
                i += 2

        return c


if __name__ == "__main__":
    a = [10, 15, 20]
    b = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    x = [0, 2, 2, 1]

    print(Solution().min_cost_climbing(x))
