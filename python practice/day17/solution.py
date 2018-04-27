import sys
class Calculator:
    def power(n,p):
        if p < 0 or n < 0:
            print('n and p should be non-negative')
        z = 1 
        for i in range(0,p):
            z = z*n
        return z;
n,p = input().split()
p = int(p)
n = int(n)
print(Calculator.power(n,p))
