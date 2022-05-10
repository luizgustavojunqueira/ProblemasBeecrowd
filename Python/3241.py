n = int(input())

for i in range(n):
    entrada = input()
    if entrada == "P=NP":
        print("skipped")
    else:
        op1, op2 = map(int, entrada.split("+"))
        print(op1 + op2)