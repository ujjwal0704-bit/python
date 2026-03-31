#n = int(input())
def fact(n):
     if n==2:
        return 2
     else:
        n = n * fact(n-1)
        return n
print(fact(5))



