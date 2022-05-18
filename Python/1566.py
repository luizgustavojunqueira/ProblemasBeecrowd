# # import sys

# # n = int(input())

# # for i in range(n):

# #     x = int(input())
    
# #     alturas = []

# #     for j in range(210):
# #         alturas.append(0)
    
# #     altura = 0

# #     while True:
# #         char = sys.stdin.readline(1)
        

# #         if char == '\n':
# #             alturas[altura] += 1
# #             altura = 0
# #             break
    

# #         if char != " ":
# #             altura = altura * 10 + int(char)
# #         else:
# #             alturas[altura] += 1
# #             altura = 0


# def countingSort(vetor, maior):
#     m = maior + 1
#     count = [0] * m
#     for i in vetor:
#         count[i] += 1
#     j = 0
#     for i in range(m):
#         for k in range(count[i]):
#             vetor[j] = i
#             j += 1
#     return vetor

# n = int(input())

# while n:
#     n -= 1

#     x = int(input())
#     vetor = input().split()

#     for i in range(x):
#         vetor[i] = int(vetor[i])

#     vetor = countingSort(vetor, max(vetor))

#     print(' '.join(str(x) for x in vetor))