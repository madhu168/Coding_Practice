def reverseBits(n):
    # Write your code here.
    if(n == 0):
        return 0;
    # make sure bits are within 32 bits range    
    n = n & 0xFFFFFFFF;
    # convert into bits and remove first 2 letters(0b)
    n = bin(n)[2:];
    # adds 0 values padding to make sure there are 32 bits
    n = n.zfill(32);
    # reversing a string in python
    n = n[::-1];
    # bits to integer is just int(number, with what bits were made)
    return int(n,2);

