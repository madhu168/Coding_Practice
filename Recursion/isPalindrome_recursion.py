def isPanlindromeHelper(l: int,r: int,s: str) -> bool:
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return isPanlindromeHelper(l+1,r-1,s)

def isPalindrome(s: str) -> bool:
    # Write your code here.
    return isPanlindromeHelper(0,len(s)-1,s)