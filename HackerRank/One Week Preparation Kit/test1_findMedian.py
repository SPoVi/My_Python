def findMedian(arr):
    # Write your code here
    arr.sort()
    print(arr)

    pos = n // 2
    print(pos)
    print(arr[pos])


if __name__ == '__main__':

    #n = int(input().strip())
    n = 5
    #arr = list(map(int, input().rstrip().split()))
    arr = [5, 3, 1, 2, 4]
    result = findMedian(arr)
