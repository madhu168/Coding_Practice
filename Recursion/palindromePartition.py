class Solution:
    def isPalindrome(self,s:str,i:int,j:int) -> bool:
        while i <= j:
            if s[i] != s[j]:
                return False
            i,j = i+1, j-1
        return True
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                ans.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return ans