#code
n=int(input())
while(n>0):
    y=int(input())
    l=list(map(int,input().split()))
    x=l.count(0)
    n=n-1
    print(x)
