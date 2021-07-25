import string
def swap_case(s):
    return string.swapcase(s)

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
