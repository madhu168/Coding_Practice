class Solution:
    def value(self, s:str) -> int:
        if s == 'I':
            return 1
        if s == 'V':
            return 5
        if s == 'X':
            return 10
        if s == 'L':
            return 50
        if s == 'C':
            return 100
        if s == 'D':
            return 500
        if s == 'M':
            return 1000
    
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            s1 = self.value(s[i])
            if i + 1 < len(s):
                s2 = self.value(s[i+1])
                
                if s1 >= s2:
                    res = res + s1
                    i = i + 1
                else:
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1
        return res
        