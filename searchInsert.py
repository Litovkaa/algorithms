# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int, mid_ind: int = 0) -> int:
        if len(nums) == 1 and nums[0] != target:
            return mid_ind + 1 if target > nums[0] else mid_ind

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        if nums[mid] < target:
            return self.searchInsert(right, target, mid_ind=mid_ind + mid)
        elif nums[mid] > target:
            return self.searchInsert(left, target, mid_ind=mid_ind)
        else:
            return mid_ind + mid


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6, 7, 8, 9, 10]
    target = 2

    print(s.searchInsert(nums, target))