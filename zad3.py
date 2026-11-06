from collections import*
def s(n):
    counts=Counter(n)
    points=0
    for i, j in counts.items():
            
        if i>=3:
            points+=1000 if j==1 else j*100
            i-=3
        if j==1:
            points+=i*100
        if j==5:
            points+=i*50
    return points
print(s([5, 1, 3, 4, 1]))
