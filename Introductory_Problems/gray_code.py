n=int(input())
for i in range(1<<n):
    val=bin(i^(i>>1))[2:]
    if len(val)<n:
        print(("0")*(n-len(val))+str(val))
    else:
        print(val)
