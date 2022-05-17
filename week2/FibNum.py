import sys
def fibNum (n):
    if n <= 1:
        return n
    prev = 0
    current = 1
    for i in range (n-1):
        prev, current = current, current+prev
    return current


if __name__ == '__main__':
    n=int(input())
    print(fibNum(n))
