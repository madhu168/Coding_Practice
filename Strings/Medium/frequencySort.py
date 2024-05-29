class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        sorted_keys = dict(sorted(d.items(),key=lambda item: item[1],reverse = True))
        ans = ""
        for key, value in sorted_keys.items():
            ans = ans + key * value
        return ans