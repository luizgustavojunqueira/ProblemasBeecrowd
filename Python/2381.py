n, k = map(int, input().split())

alunos = []

for i in range(n):
    alunos.append(input())

alunos.sort()

print(alunos[k-1])