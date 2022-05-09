for i in range(7):
    if i == 0 or i == 6:
        for j in range(39):
            print("-", end = "")
    else:
        for j in range(39):
            if j == 0 or j == 38:
                print("|", end = "")
            else:
                print(" ", end = "")
                
    print()