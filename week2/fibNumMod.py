def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
        = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def fibNum(n, m):
     
    # Getting the period
    pisano_period = pisanoPeriod(m)
     
    # Taking mod of N with
    # period length
    n = n % pisano_period
    if n <= 1:
        return n
    prev = 0
    current = 1
    for i in range (n-1):
        prev, current = current%m, (current+prev)%m
    return current


if __name__ == '__main__':
    a, b=map(int, input().split())
    print(fibNum(a,b))