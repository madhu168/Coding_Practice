class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_counter = 0
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                max_counter = max(max_counter,counter)
                counter -= 1
        return max_counter