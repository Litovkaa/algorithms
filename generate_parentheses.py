class Solution:
    def generate_parenthesis(self, n: int, s: str = "(") -> List[str]:
        o = len([el for el in s if el == "("])
        c = len([el for el in s if el == ")"])
        if o == n and c == n:
            return [s]

        if o >= c:
            if o < n:
                return self.generateParenthesis(n, s=s+"(") + self.generateParenthesis(n, s=s+")")
            else:
                return self.generateParenthesis(n, s=s+")")
        else:
            return []