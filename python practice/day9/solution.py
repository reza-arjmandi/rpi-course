###########################################################
#                                                         #
#    Solving factorial problem with recursive function    #
#                                                         #
###########################################################
def factorial(n):
    if n == 2:
        return 2
    return n * factorial(n - 1)
  
print(factorial(int(input())))