decimal = int(input())
binary = bin(decimal)

parts = str(binary)[2:].split('0')

max = 0
for part in parts:
    if(len(part)>max):
        max=len(part)

print(max)