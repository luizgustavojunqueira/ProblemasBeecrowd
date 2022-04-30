from math import sqrt

n = int(input())

fib = ( ( (1+sqrt(5)) / 2 ) ** n - ( (1-sqrt(5)) / 2 ) ** n  ) / sqrt(5)

print(f"{fib:.1f}")