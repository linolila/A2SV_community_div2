if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    hashed = hash(integer_list)
    print(hashed)
