from math import ceil
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lenA, lenB = len(a), len(b)
        repetetions = ceil(lenB / lenA)
        repeatedA = a * repetetions

        for i in range(3):
            if b in repeatedA:
                return repetetions
            repeatedA += a
            repetetions += 1
        
        return -1