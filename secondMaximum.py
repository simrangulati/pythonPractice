def find_second_max(arr):
    first = second = float('-inf')
    for element in arr:
        if element > first:
            second = first
            first = element
        elif first > element > second:
            second = element

    return second

if __name__ == "__main__":
    n=int(input())
    arr = map(int, input().split())

    # 2 3 4 4 6 5
    secondMax=find_second_max(arr)
    print("Second maximum is "+ str(secondMax))
