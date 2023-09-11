# https://leetcode.com/problems/number-of-provinces/
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected)
        dct = {i: [] for i in range(l)}

        for i in range(l):
            for j in range(l):
                if i != j and isConnected[i][j] == 1:
                    dct[i] += [j]

        prov = 0
        visited = []
        for k, v in dct.items():
            if k not in visited:
                visited.append(k)
                while v:
                    nxt = v.pop(0)
                    if nxt not in visited:
                        visited.append(nxt)
                        for v1 in dct[nxt]:
                            v.append(v1)

                prov += 1

        return prov


if __name__ == "__main__":
    is_con = [[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]

    print(Solution().findCircleNum(is_con))
