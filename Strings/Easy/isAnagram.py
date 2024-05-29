class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d1 = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in range(len(t)):
            if t[i] in d1:
                d1[t[i]] += 1
            else:
                d1[t[i]] = 1

        if d == d1:
            return True
        else:
            return False