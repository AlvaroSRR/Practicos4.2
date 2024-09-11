num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero: "))
num3=float(input("ingrese un numero: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1>num2:
        if num1 > num3:
            print(f"el numero mayor es {num1}")
        else:
            print(f"el numero mayor es {num3}")
    else:
        if num2 > num3:
            print(f"el numero mayor es {num2}")
        else:
            print(f"el numero mayor es {num3}")
else:
    print(f"los numeros son iguales")