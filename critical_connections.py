#https://leetcode.com/problems/critical-connections-in-a-network/
# TODO: РЕШИТЬ ЗАДАЧКУ
from typing import List
from functools import reduce


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    dct = {i: set() for i in range(n)}
    for conn in connections:
        for i in [0, 1]:
            dct[conn[i]].update([conn[abs(i - 1)]])

            curr = [el for el in dct[conn[i]] if el not in conn]
            if len(dct[conn[i]]) < n:
                for _c in curr:
                    dct[conn[i]].update(dct[_c])

    for k, v in dct.items():
        if len(v) < n-1:
            print(k)
    print(dct)

if __name__ == "__main__":
    critical_connections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[3,5],[4,5]])