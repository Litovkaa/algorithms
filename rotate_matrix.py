# https://leetcode.com/problems/rotate-image/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return matrix

        steps = len(matrix) // 2
        l, r = (0, -1)
        m = [el.copy() for el in matrix]
        for _ in range(steps):
            for j in range(len(matrix)):
                matrix[l][-(j + 1)] = m[j][l]
                matrix[r][-(j + 1)] = m[j][r]

            print(matrix)

            for i in range(len(matrix)):
                matrix[i][r] = m[l][i]
                matrix[i][l] = m[r][i]

            l += 1
            r -= 1

        return matrix


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    print(sol.rotate(matrix))
