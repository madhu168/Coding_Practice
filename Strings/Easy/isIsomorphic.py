class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charCount = {}
        c = "a"
        for i in range(len(s)):
            if s[i] in charCount:
                c = charCount[s[i]]
                if c != t[i]:
                    return False
            elif t[i] not in charCount.values():
                charCount[s[i]] = t[i]
            else:
                return False   
        
        return True