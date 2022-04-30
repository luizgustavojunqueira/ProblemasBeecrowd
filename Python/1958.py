mantissa = float(input())
exp = 0

sinalPositivo = True

if mantissa <= 0:
    if str(mantissa) != "0.0":
        sinalPositivo = False
    mantissa = abs(mantissa)


if 0 < mantissa < 1:

    while mantissa < 1:
        mantissa = mantissa * 10
        exp += 1  

    if sinalPositivo:
        print(f"+{mantissa:.4f}E-{exp:02d}")
    else:
        print(f"-{mantissa:.4f}E-{exp:02d}")

else:

    while mantissa > 9:
        mantissa = mantissa / 10
        exp += 1 
    
    if sinalPositivo:
        print(f"+{mantissa:.4f}E+{exp:02d}")
    else:
        print(f"-{mantissa:.4f}E+{exp:02d}")