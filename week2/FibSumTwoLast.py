def fibNum(a, b):
    if b <= 1:
        return b
    prev1 = 0
    current1 = 1
    prev2 = 0
    current2 = 1
    sum1 = 1
    sum2 = 1
    for i in range (a-2):
        prev1, current1 = current1%10, (current1+prev1)%10
        sum1 = (sum1 + current1)%10
    for i in range (b-1):
        prev2, current2 = current2%10, (current2+prev2)%10
        sum2 = (sum2 + current2)%10
    return (sum2-sum1)%10

if __name__ == '__main__':
    a, b=map(int, input().split())
    print(fibNum(a,b))