n = int(input())
temp = n
power = len(str(n))
sum_val = 0

while n > 0:
    digit = n % 10
    sum_val += digit ** power
    n //= 10

print("Armstrong" if temp == sum_val else "Not Armstrong")