# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150

from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        total_mult = reduce(lambda a, b: a * b, nums)

        for el in nums:
            if el > 0:
                e = int(total_mult * (el ** -1))
            else:
                e = int(total_mult)
            out.append(e)

        return out


if __name__ == "__main__":
    a = [1, 2, 3]
    i = 5
    print(a[i:] + a[:i])