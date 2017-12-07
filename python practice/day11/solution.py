#################################################################
#                                                               #
#     Solution to find the maximum sum of elements in whole     #
#          hourglass shapes of an two dimensional array         #
#                                                               #
#################################################################

matrixDimension = 6

matrix = [[0 for x in range(matrixDimension)] for y in range(matrixDimension)]

for i in range(matrixDimension):
    for j in range(matrixDimension):
        matrix[i][j] = int(input())


max = 0
rowAdder = 0
columnAdder = 0

for i in range(matrixDimension - 2):
    for j in range(matrixDimension - 2):
        sum = 0
        for k in range(3):
            for l in range(3):
                sum += matrix[i+k][j+l]
        sum -= matrix[i+1][j] + matrix[i+1][j+2]
        if max < sum:
            max = sum

print(max)
