def countDigits(n: int) -> int:
    c = 0;
    a = n;
    if(n >= 1):
        while(n >= 10):
            b = n % 10;
            n = n//10;
            if((b != 0) and (a%b) == 0):
                c+=1;
        if((n != 0) and (a%n) == 0):
            c+=1;
    return c;