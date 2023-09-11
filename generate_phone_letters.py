# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from functools import reduce


def letter_combs(digits: str):
    digs_lets = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }

    def all_pairs(a1, a2):
        res = []
        for el1 in a1:
            for el2 in a2:
                res.append(el1 + el2)
        return res

    letter_arrs = [digs_lets[int(k)] for k in digits]
    return reduce(all_pairs, letter_arrs)


if __name__ == "__main__":
    print(letter_combs("2345"))


