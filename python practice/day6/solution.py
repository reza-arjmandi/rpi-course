T = int(input())
string = []
for i in range(T):
    string.append(input())
    
for i in range(T):
    for j in range(0,len(string[i]),2):
        print(string[i][j],end="")
        
    print(end=" ")
    
    for j in range(1,len(string[i]),2):
        print(string[i][j],end="")
        
    print("")
        