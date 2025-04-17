t=int(input())
for k in range(1,t+1):
    n=(k*k*(k*k-1))//2
    if k>2:
        att=4*(k-1)*(k-2)
    else:
        att=0
    print(n-att)
    
