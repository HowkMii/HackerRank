def is_leap(a):
    if a % 400 ==0:
        return True
    if a % 100 == 0:
        return False
    if a % 4 == 0:
        return True
    return False

year = int(input())
print(is_leap(year))
