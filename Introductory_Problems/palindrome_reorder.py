n=input()
d={}
for i in n:
    if i not in d:
        d[i]=n.count(i)
o,m,l=0,"",""
for i in sorted(d):
    if d[i]%2==1:
        o+=1
        m+=i*o
    l+=i*(d[i]//2)
if o>1:
    print("NO SOLUTION")
else:
    print(l+m+l[::-1])
