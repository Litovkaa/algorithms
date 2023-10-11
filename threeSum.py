# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dct = {}
        nums = sorted(nums)
        for i, el in enumerate(nums):
            if el in dct:
                dct[el] += [i]
            else:
                dct[el] = [i]

        subs = set()
        for i in range(len(nums)):
            el = nums[i]
            for j in range(i + 1, len(nums)):
                el1 = nums[j]
                diff = 0 - el - el1
                if diff in dct:
                    for x in dct[diff]:
                        if x != i and x != j:
                            if diff <= el:
                                sub = (diff, el, el1)
                            elif diff >= el1:
                                sub = (el, el1, diff)
                            else:
                                sub = (el, diff, el1)

                            if sub not in subs:
                                subs.add(sub)

                            break

        return subs





