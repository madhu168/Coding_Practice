import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        ans = s[::-1]
        if(ans.casefold() == s.casefold()):
            return True
        else:
            return False