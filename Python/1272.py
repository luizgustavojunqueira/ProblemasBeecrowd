n = int(input())

for i in range(n):
    msg = ""
     
    frase = input().replace("·", " ").split()
    
    for j in range(len(frase)):
        msg += frase[j][0]
        
    print(msg)