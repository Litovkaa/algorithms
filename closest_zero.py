from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        queue = deque()

        def check_valid(x, y):
            x_val = 0 <= x < rows
            y_val = 0 <= y < cols
            return x_val and y_val

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = float("inf")

        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                if check_valid(r+dr, c+dc):
                    if mat[r+dr][c+dc] > mat[r][c] + 1:
                        mat[r+dr][c+dc] = mat[r][c] + 1
                        queue.append((r+dr, c+dc))

        return mat

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1, 1, 1],
          [1, 1, 0],
          [0, 1, 1]], [[2, 2, 1], [1, 1, 0], [0, 1, 1]]),
        ([[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
        ([[0, 0, 0],
          [1, 1, 0],
          [1, 1, 1]], [[0, 0, 0], [1, 1, 0], [2, 2, 1]]),
        ([[1, 1, 1],
          [1, 1, 0],
          [1, 1, 1]], [[3, 2, 1], [2, 1, 0], [3, 2, 1]]),
        ([[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    ]
    for i, test in enumerate(tests):
        ans = sol.updateMatrix(test[0])
        if ans == test[1]:
            print(f"Passed test {i}")
        else:
            print(f"Incorrect answer for test {i}")
            print(f"Answer: {ans}")
            print(f"Correct answer: {test[1]}")
