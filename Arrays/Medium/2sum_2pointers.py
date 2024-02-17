def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    book.sort()
    left = 0
    right = len(book) - 1
    while(left < right):
        s = book[left] + book[right]
        if(s == target):
            return "YES"
            break
        elif(s < target):
            left += 1
        else:
            right -= 1
    return "NO"
