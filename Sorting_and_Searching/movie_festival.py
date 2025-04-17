n=int(input())
arr=[]
for i in range(n):
    s,e=map(int,input().split())
    arr.append([s,e])
arr.sort(key=lambda x:x[1])
c=0
e=0
for st,en in arr:
    if st>=e:
        c+=1
        e=en
print(c)
