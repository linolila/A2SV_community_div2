if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(1,len(arr)):
        if arr[i - 1] > arr[i]:
            print(arr[i])
            break;
        
        
