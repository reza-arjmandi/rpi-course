################################################
#                                              #
#    Solution to find the maximum number of    #
#      consecutive 1's in a decimal digit      #
#                                              #
################################################

num = int(input())
maximum = 0
count = 0

while num > 0:
    if num % 2 == 1:
        count += 1
        if count > maximum:
            maximum = count
    else:
        count = 0
    num = int(num / 2)
print(maximum)
