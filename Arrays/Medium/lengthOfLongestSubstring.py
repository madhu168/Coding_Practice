class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s.strip()) == 0 or len(s) == 1:
            return 1
        hash_map = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in hash_map:
                start = max(start,hash_map[s[i]]+1)
            hash_map[s[i]] = i
            max_len = max(max_len,i-start+1)
        return max_len