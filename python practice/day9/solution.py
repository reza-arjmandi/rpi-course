def Factorial(N):
    if(N==0):
        return 1
    else:
        return Factorial(N-1)*N

num = int(input())
print(Factorial(num))
