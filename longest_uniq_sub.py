# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# "abcc" -> "abc"
# "dbdhfkl" -> "dbdhfkl"
# "nikita" -> "kita"

def longest_uniq_sub(s: str) -> str:
    i = 0
    dct = {}
    res_dct = {}
    while i < len(s):
        val = s[i]
        if val in dct:
            if len(dct) > len(res_dct):
                res_dct = dct

            dct = {k: v for k, v in dct.items() if v > dct[val]}
            continue
        else:
            dct[val] = i
            i += 1

    if len(dct) > len(res_dct):
        res_dct = dct

    out = "".join(sorted(res_dct.keys(), key=lambda x: res_dct[x]))
    return out


if __name__ == "__main__":
    print(longest_uniq_sub("aaaaa"))
    print(longest_uniq_sub("nikita"))



