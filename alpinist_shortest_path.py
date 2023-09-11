# https://www.codewars.com/kata/576986639772456f6f00030c/train/python

from collections import deque


def path_finder(surf: str):
    mat = [list(map(int, list(el))) for el in surf.split("\n")]
    rows = cols = len(mat)
    dirs = {(0, 1), (1, 0), (-1, 0), (0, -1)}

    dists = {(r, c): float("inf") for c in range(cols) for r in range(rows)}
    dists[(0, 0)] = 0

    visited_nodes = deque()
    queue = deque([(0, 0)])

    def check_valid(x, y):
        x_val = 0 <= x < rows
        y_val = 0 <= y < cols
        return x_val and y_val

    while queue:
        x, y = queue.popleft()
        visited_nodes.append((x, y))
        for dx, dy in dirs:
            if check_valid(x + dx, y + dy):
                dist = abs(mat[x + dx][y + dy] - mat[x][y]) + dists[(x, y)]
                if dist < dists[(x + dx, y + dy)]:
                    dists[(x + dx, y + dy)] = dist
                    queue.append((x + dx, y + dy))

    return dists[(rows - 1, cols - 1)]


if __name__ == "__main__":
    h = "\n".join([
        "0899",
        "9059",
        "9159",
        "9965",
    ])

    z = "\n".join([
        "77777",
        "00007",
        "77777",
        "70000",
        "77777"
    ])

    a = "\n".join([
        "000",
        "000",
        "000"
    ])

    b = "\n".join([
        "010",
        "010",
        "010"
    ])

    c = "\n".join([
        "010",
        "101",
        "010"
    ])

    d = "\n".join([
        "0707",
        "7070",
        "0707",
        "7070"
    ])

    e = "\n".join([
        "700000",
        "077770",
        "077770",
        "077770",
        "077770",
        "000007"
    ])

    f = "\n".join([
        "777000",
        "007000",
        "007000",
        "007000",
        "007000",
        "007777"
    ])

    g = "\n".join([
        "000000",
        "000000",
        "000000",
        "000010",
        "000109",
        "001010"
    ])

    tests = [(a, 0), (b, 2), (c, 4), (d, 42), (e, 14), (f, 0), (g, 4), (h, 13), (z, 0)]
    for i, test in enumerate(tests):
        ans = path_finder(test[0])
        if ans == test[1]:
            print(f"Passed test {i}")
        else:
            print(f"Incorrect answer for test {i}")
            print(f"Answer: {ans}")
            print(f"Correct answer: {test[1]}")

    #print(path_finder(z))
