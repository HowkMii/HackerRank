def count_substring(string, sub_string):
    a=len(string)
    s=len(sub_string)
    b=0
    for i in range(a-s+1):
        if(string[i:(i+s)]==sub_string):
            b=b+1
    return b

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
