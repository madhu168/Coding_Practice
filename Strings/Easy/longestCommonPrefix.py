class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 0:
            return ""

        if size == 1:
            return strs[0]

        strs.sort()

        prefix = ""
        end = min(len(strs[0]),len(strs[size-1]))

        i = 0

        while( i < end and strs[0][i] == strs[size-1][i]):
            i += 1

        prefix = strs[0][:i]
        return prefix