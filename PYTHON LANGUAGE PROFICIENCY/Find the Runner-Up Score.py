if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a=max(arr)
    c=arr.count(a)
    for i in range(c):
        arr.remove(a)
    print(max(arr))
