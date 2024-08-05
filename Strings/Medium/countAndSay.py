class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(2,n+1):
            streak = 0
            prev = ""
            res = ""
            for c in s:
                if prev == "" or prev == c:
                    streak += 1
                else:
                    res += str(streak) + prev
                    streak = 1
                prev = c
            res += str(streak) + prev
            s = res
        return s