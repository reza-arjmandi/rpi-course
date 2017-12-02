numberOfInputs = int(input())

phoneBook = {}
while numberOfInputs>0:
    name_number = input().split()
    phoneBook[name_number[0]]=name_number[1]
    numberOfInputs-=1

query = []
while True:
   nameQuery = input()
   if (nameQuery =='') :
       break
   query.append(nameQuery)

for i in range(len(query)) :
    if query[i] in phoneBook :
        print(query[i] + "=" + phoneBook[query[i]])
    else:
        print("Not found")
