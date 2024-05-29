class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a = []
        ans = ""
        for i in range(len(s)):
            if s[i] == "(":
                a.append(s[i])
                if len(a) > 1:
                    ans = ans + s[i]
            if s[i] == ")":
                if len(a) > 1:
                    ans = ans + s[i]
                a.remove(a[-1])
        return ans