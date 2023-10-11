# Example:
# nums1 = [0, 0, 3, 40, 0, 0, 0, 5, 0]
# nums2 = [1, 0, 0, 2, 0, 14, 0, 0, 0]
# res = 80
# Write function dot_prod without using hash-tables

import time
import numpy as np
import matplotlib.pyplot as plt

class SparseVector:
    def __init__(self, vec):
        self.nums = []
        self.inds = []
        for i, el in enumerate(vec):
            if el != 0:
                self.nums += [el]
                self.inds += [i]

    def dot_prod(self, vec: 'SparseVector') -> int:
        commons = [el1 for el1 in self.inds if el1 in vec.inds]
        res = 0
        for c in commons:
            vec1_i = self.inds.index(c)
            vec2_i = vec.inds.index(c)
            res += self.nums[vec1_i] * vec.nums[vec2_i]

        return res

    def dot_prod_opt(self, vec: 'SparseVector') -> int:
        short, long = (self, vec) if len(self.inds) < len(vec.inds) else (vec, self)
        i_s = i_l = res = 0

        while i_s < len(short.inds) and i_l < len(long.inds):
            i1 = short.inds[i_s]
            i2 = long.inds[i_l]
            if i1 == i2:
                res += short.nums[i_s] * long.nums[i_l]
                i_s += 1
                i_l += 1
            elif i1 < i2:
                i_s += 1
            else:
                i_l += 1

        return res


if __name__ == "__main__":
    def timeit(func, arg):
        s_t = time.time()
        func(*arg)
        f_t = time.time()
        return f_t - s_t

    def dummy_fun(n1, n2):
        res = sum([e1*e2 for e1, e2 in zip(n1, n2)])
        return res

    def res_fun(n1, n2):
        vec1 = SparseVector(n1)
        vec2 = SparseVector(n2)
        return vec1.dot_prod(vec2)

    def res_fun_opt(n1, n2):
        vec1 = SparseVector(n1)
        vec2 = SparseVector(n2)
        return vec1.dot_prod_opt(vec2)

    def gen_inp(size):
        dens = 0.25
        n = []
        for _ in range(size):
            if np.random.rand() < dens:
                n += [np.random.randint(-1e3, 1e3)]
            else:
                n += [0]
        return n

    for _ in range(1000):
        n1 = gen_inp(100)
        n2 = gen_inp(100)
        dummy_res = dummy_fun(n1, n2)
        res = res_fun(n1, n2)
        res_opt = res_fun_opt(n1, n2)
        if res == dummy_res:
            #print(f"M*N solution passed on iteration {_}")
            pass
        else:
            print(f"M*N solution FAILED!!")
            break

        if res_opt == dummy_res:
            #print(f"N solution passed on iteration {_}")
            pass
        else:
            print(f"N solution FAILED!!")
            break

    time_res, time_res_opt, approx1, approx2 = [], [], [], []
    for _ in range(1, 1000):
        n1 = gen_inp(_)
        s1 = len([el for el in n1 if el != 0])
        n2 = gen_inp(_)
        s2 = len([el for el in n2 if el != 0])
        time_res.append(timeit(res_fun, [n1, n2]))
        approx1.append(s1*s2)
        time_res_opt.append(timeit(res_fun_opt, [n1, n2]))
        approx2.append(s1 if s1 < s2 else s2)

    plt.plot(time_res, c="blue", ls="-", label="O(M*N)")
    #plt.plot(approx1, c="green", ls=":", label="O(M*N) approx")
    plt.plot(time_res_opt, c="red", ls='-', label="O(N)")
    #plt.plot(approx2, c="yellow", ls=":", label="O(N) approx")
    plt.legend()
    plt.show()