# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        max_l = ""

        def incr_width(i_left: int, i_right: int) -> str:
            _ = ""
            while i_left >= 0 and i_right < len(s):
                if s[i_left] == s[i_right]:
                    _ = s[i_left:i_right + 1]
                    i_left -= 1
                    i_right += 1
                elif s[i_left] == s[i_right-1]:
                    if s[i_left:i_right] == s[i_left:i_right][::-1]:
                        _ = s[i_left:i_right]
                    return _
                elif s[i_right] == s[i_left+1]:
                    if s[i_left+1:i_right+1] == s[i_left+1:i_right+1][::-1]:
                        _ = s[i_left+1:i_right+1]
                    return _
                else:
                    return _
            return _

        for i in range(len(s)):
            if i+1 < len(s) and i-1 >= 0 and s[i + 1] == s[i - 1]:
                _ = incr_width(i, i)
            elif i+1 < len(s) and s[i] == s[i + 1]:
                _ = incr_width(i, i + 1)
            else:
                continue

            max_l = max([_, max_l], key=len)

        return max_l if len(max_l) > 0 else s[0]


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    def gen_palindrome(n):
        lets = np.random.choice(["a", "b", "c", "d", "e", "f", "g"], n//2)
        lets = "".join(lets)
        if len(lets) * 2 < n:
            return lets + "x" + lets[::-1]
        return lets + lets[::-1]

    print(gen_palindrome(6))

    # print(Solution.longest_palindrome(s1))
    # print(Solution.longest_palindrome(s2))
    # print(Solution.longest_palindrome(s3))
    # print(Solution.longest_palindrome(s5))
    # print(Solution.longest_palindrome(s6))
