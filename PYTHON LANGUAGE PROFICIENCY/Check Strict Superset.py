# Enter your code here. Read input from STDIN. Print output to STDOUT
l =set(map(int,input().split()))
n = int(input())
val =""
for i in range(n):
    l1 = set(map(int,input().split()))
    if len(l1.difference(l))==0:
        val ="True"
    else:
        val= "False"
        break
print(val)