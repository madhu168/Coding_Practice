class Solution:
    def reverse(self, x: int) -> int:
        if((x < -2**31) or (x > (2**31)-1)):
            return 0;
        z = x;
        if(x < 0):
            x = x * -1;
        rev = 0
        while(x >= 10):
            b = x % 10
            x = x // 10
            rev = rev * 10 + b
        if((x != 0) and (x < 10)):
            rev = rev * 10 + x
        if(z < 0):
            rev = rev * -1;
        if((rev < -2**31) or (rev > (2**31)-1)):
            return 0;
        return rev;