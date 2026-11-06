def rsum(n):
    start=n*(n-1)+1
    end=n*(n+1)-1
    num=range(1, end+1, 2)
    res=sum(filter(lambda x: start<=x<=end, num))
    return res
n=int(input())
print(rsum(n))
