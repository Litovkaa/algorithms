# https://leetcode.com/problems/network-delay-time/description/
from typing import List


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    dct = {i: float("inf") for i in range(1, n+1) if i != k}
    dct[k] = 0

    def dfs(conns, k):
        paths = sorted([con for con in conns if con[0] == k], key=lambda x: x[2])
        for path in paths:
            _, new_k, t = path
            if dct[k] + t < dct[new_k]:
                dct[new_k] = dct[k] + t
                dfs(conns, new_k)

        return

    dfs(times, k)
    res = max(dct.values())
    return res if res != float("inf") else -1


def network_delay_time_dijkstra(times: List[List[int]], n: int, k: int) -> int:
    dct = {i: float("inf") for i in range(1, n + 1) if i != k}
    dct[k] = 0

    queue = [(k, 0)]

    while queue:
        curr_k, curr_t = queue.pop(0)
        conns = [(con[1], con[2]) for con in times if con[0] == curr_k]

        for new_k, new_t in conns:
            if curr_t + new_t < dct[new_k]:
                dct[new_k] = curr_t + new_t
                queue.append((new_k, dct[new_k]))

        queue = sorted(queue, key=lambda x: x[1])

    res = max(dct.values())
    return res if res != float("inf") else -1

if __name__ == "__main__":
    conns = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print(network_delay_time_dijkstra(conns, n, k))