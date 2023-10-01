# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    @staticmethod
    def trap(height: List[int]) -> int:
        depth = l = 0

        def ltr(arr):
            nonlocal depth
            nonlocal l
            d = 0
            i = 1
            while i < len(arr):
                left = arr[l]
                h = arr[i]

                if left - h > 0:
                    d += left - h
                else:
                    l = i
                    depth += d
                    d = 0

                i += 1

        ltr(height)
        if l < len(height) - 1:
            back = height[l:][::-1]
            l = 0
            ltr(back)

        return depth


if __name__ == "__main__":
    tests = {
        (0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1): 6,
        (4, 2, 0, 3, 2, 5): 9
    }

    for t in tests:
        if Solution.trap(list(t)) == tests[t]:
            print(True)
