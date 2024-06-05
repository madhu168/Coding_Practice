from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        string_length = len(s)
        for i in range(string_length):
            char_counter = Counter()
            for j in range(i, string_length):
                char_counter[s[j]] += 1
                current_beauty = max(char_counter.values()) - min(char_counter.values())
                total_beauty += current_beauty
        return total_beauty