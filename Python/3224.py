podeDizer = input()
ahMedico = input()

if len(ahMedico[:len(ahMedico)-1]) <= len(podeDizer[:len(podeDizer)-1]):
    print("go")
else:
    print("no")