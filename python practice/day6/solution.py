N = int(input())
#length N that is indexed from 0 to N-1
for i in range(0, N):

    string = input()
#even-indexed
    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end="")

    print(" ", end="")
#odd-indexed
    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end="")

    print("")
