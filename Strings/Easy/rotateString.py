class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        while s != goal and i < len(s):
            first = s[0]
            rest = s[1:]
            s = rest + first
            i += 1
            if s == goal:
                break

        if i == len(s):
            return False
        else:
            return True
