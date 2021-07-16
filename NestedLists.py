if __name__ == '__main__':
   dic={}
   s= list()

for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in dic:
        dic[score].append(name)
    else:
        dic[score]=[name]
    if score not in s:
        s.append(score)
m=min(s)
s.remove(m)
m1=min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)
