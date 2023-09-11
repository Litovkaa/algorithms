# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        pos = [el for el in nums if el >= 0]
        neg = [abs(el) for el in nums if el < 0][::-1]

        ns = []
        while pos and neg:
            if pos[0] < neg[0]:
                p = pos.pop(0)
                ns.append(p)
            else:
                n = neg.pop(0)
                ns.append(n)

        if not pos or not neg:
            n = pos if pos else neg
            if n:
                for el in n:
                    ns.append(el)

        return list(map(lambda x: x ** 2, ns))


def timeit(func):
    def wrapper(*args, **kwargs):
        s_t = time.time()
        func(*args, **kwargs)

        f_t = time.time()
        return f_t - s_t

    return wrapper


if __name__ == "__main__":
    import numpy as np
    import time
    import matplotlib.pyplot as plt
    from bigO import BigO

    @timeit
    def time_ss(nums):
        s = Solution()
        s.sorted_squares(nums)

    print(time_ss([3, 2, 1]))

    times = []
    for n in range(1, 100000, 100):
        nums = np.random.choice(range(-10000, 10000), n)
        times.append(time_ss(nums))

    plt.plot(times)
    plt.show()

    sol = Solution()
    lib = BigO.BigO()
    print(lib.test(sol.sorted_squares, "sorted"))