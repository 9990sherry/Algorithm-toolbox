def max_pair (arrsize, arr):
    largest = 0
    second_largest = 0
    for i in range(arrsize):
        if (arr[i] > largest):
            second_largest=largest
            largest = arr[i]
        elif (arr[i] > second_largest):
            second_largest = arr[i]
    return largest*second_largest

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pair(input_n,input_numbers))