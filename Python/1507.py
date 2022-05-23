def ehSubSequencia(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    index_str1 = 0  
    index_str2 = 0  

    while index_str1 < len_str1 and index_str2 < len_str2:
        if str1[index_str1] == str2[index_str2]:
            index_str1 = index_str1 + 1
        index_str2 = index_str2 + 1
        
    return index_str1 == len_str1

        
n = int(input())

for i in range(n):
    s = input()
    q = int(input())

    for i in range(q):
        r = input()
        
        if ehSubSequencia(r, s):
            print("Yes")
        else:
            print("No")
        