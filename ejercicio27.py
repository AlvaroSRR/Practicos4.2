num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero: "))
if num1!= num2:
    if num1>num2:
        print(f"el numero mayor es {num1}")
    else:
        print(f"el numero mayor es {num2}")
else:
    print(f"los numeros son iguales")