# https://leetcode.com/problems/text-justification/
from typing import List


class Solution:
    @staticmethod
    def full_justify(words: List[str], max_width: int) -> List[str]:
        row = []
        rs = []
        for i in range(len(words)):
            w = words[i]
            add_row = row + [w]
            if len(" ".join(add_row)) <= max_width:
                row = add_row
            else:
                if len(row) == 1:
                    row[0] = row[0].ljust(max_width, " ")
                else:
                    j = 0
                    while len(" ".join(row)) < max_width:
                        if j < len(row) - 1:
                            row[j] = row[j] + " "
                            j += 1
                        else:
                            j = 0

                rs.append(" ".join(row))
                row = [w]

        rs.append(" ".join(row).ljust(max_width, " "))
        return rs


if __name__ == "__main__":
    s = "a"
    print(s[1:])