#https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        if len(nums) == 1: return 0
        i = 0
        last_ind = len(nums) - 1
        steps = 0
        while i < last_ind:
            k = nums[i]
            if i + k >= last_ind:
                return steps + 1

            achievable = nums[i:i + k + 1]
            incr = [j + el for j, el in enumerate(achievable)]
            i = i + incr.index(max(incr))
            steps += 1

        return steps


if __name__ == "__main__":
    print(Solution.jump([2, 3, 1, 1, 4]))
    print(Solution.jump([2, 3, 0, 1, 4]))
    print(Solution.jump([2, 3, 1]))
    print(Solution.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))