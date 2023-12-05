while True:
    try:

        num = input()
        cutoff = float(input())
        numInt = 0

        if num.find(".") > -1:
            if len(num[0:num.index(".")]) > 0:
                numInt = int(num[0:num.index(".")])
        else:
            numInt = int(num)
        
        numFloat = float(num) - numInt

        if cutoff < numFloat:
            print(numInt+1)
        else:
            print(numInt)

    except EOFError:
        break