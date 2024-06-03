class Solution:
    def nums(self, s: str) -> bool:
        if s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9":
            return True
    def myAtoi(self, s: str) -> int:
        ans = ""
        s = s.strip()
        negative = False
        flag = False
        for i in range(len(s)):
            if s[i] == "-" and flag == False:
                negative = True
                flag = True
            elif s[i] == "+" and flag == False:
                negative = False
                flag = True
            elif i < len(s)-1 and s[i] == "0":
                ans = ans + s[i]
                flag = True
            elif i < len(s)-1 and s[i] == "0" and s[i+1] == "0":
                if ans != "":
                    ans = ans + s[i]
                else:
                    ans = ans + ''
            elif i == len(s)-1 and s[i] == "0":
                ans = ans + s[i]
            elif self.nums(s[i]):
                ans = ans + s[i]
                flag = True
            else:
                break
            if (s[i] == "-" or s[i] == "+") and i > 0 and (s[i-1] == "+" or s[i-1] == "-"):
                break
        if ans == "":
            ans = 0
        if negative:
            ans = -1 * int(ans)
        else:
            ans = int(ans)
        upper_limit = (2 ** 31) - 1
        lower_limit = (-2 ** 31)
        if ans > upper_limit:
            return upper_limit
        elif ans < lower_limit:
            return lower_limit
        else:
            return ans
        