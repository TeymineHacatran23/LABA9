def F(n):
    for num in n:
        if n.count(num)%2!=0:
            return num
print(F([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
