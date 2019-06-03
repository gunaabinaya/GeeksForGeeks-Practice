t=int(input())
while t>0:
    a=list(map(int,input().split()))
    n=a[0]
    k=a[1]
    l=list(map(int,input().split()))
    x=l[k:]
    y=l[:k]
    x.extend(y)
    for i in x:
        print(i,end=' ')
    print()
    t=t-1
