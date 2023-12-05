k = input()
n = int(input())
t = len(k)

aeiou = "aeiou"

for i in range(n):
    frase = input()
    
    a = -1
    
    vogal = False
    
    if len(frase) == 0 or frase[1] in aeiou:
        vogal = True
    
    for j in range(len(frase)):
        letra = frase[j]
        
        if j > 1 and frase[j-1] == ' ':
            vogal = letra in aeiou
        
        if vogal == True or letra == ' ':
            print(letra)
        else:
            a = (a + 1) % t
            print("a:", a)
            print(chr((ord(letra) + ord(k[a+1]) - 2 * ord('a')) % 26 + ord('a')))
        
    print()