n = int(input())

totalCoelhos = 0
totalRatos = 0
totalSapos = 0

for i in range(0, n):
    num, tipo = input().split()
    num = int(num)
    if tipo == "C":
        totalCoelhos += num
    elif tipo == "R":
        totalRatos += num
    elif tipo == "S":
        totalSapos += num

totalCobaias = totalRatos + totalSapos + totalCoelhos
print(f"Total: {totalCobaias} cobaias")
print(f"Total de coelhos: {totalCoelhos}")
print(f"Total de ratos: {totalRatos}")
print(f"Total de sapos: {totalSapos}")

percentCoelhos = (totalCoelhos * 100) / totalCobaias
percentSapos = (totalSapos * 100) / totalCobaias
percentRatos = (totalRatos * 100) / totalCobaias

print(f"Percentual de coelhos: {percentCoelhos:.2f} %")
print(f"Percentual de ratos: {percentRatos:.2f} %")
print(f"Percentual de sapos: {percentSapos:.2f} %")