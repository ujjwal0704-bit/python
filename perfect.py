n = int(input())
sum_div = 0

for i in range(1, n):
    if n % i == 0:
        sum_div += i

print("Perfect" if sum_div == n else "Not Perfect")