numberOfInputs = int(input())

phoneBook = {}
while numberOfInputs>0:
    name_number = input().split()
    phoneBook[name_number[0]]=name_number[1]
    numberOfInputs-=1

query = []
try:
    while(1):
        query.append(input())   
except:
    pass

for i in range(len(query)) :
    if query[i] in phoneBook :
        print(query[i] + "=" + phoneBook[query[i]])
    else:
        print("Not found")