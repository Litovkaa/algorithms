# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s): return s

        i = 0
        period = 0
        rows = ["" for _ in range(numRows)]
        up = True
        while i < len(s):
            if up:
                if period < numRows-1:
                    rows[period] += s[i]
                    period += 1
                    i += 1
                else:
                    up = not up
            else:
                if period > 0:
                    rows[period] += s[i]
                    period -= 1
                    i += 1
                else:
                    up = not up

        return "".join(rows)

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))

