num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero: "))
num3=float(input("ingrese un numero: "))
suma=num1+num2+num3
if suma>10:
    raiz=float(suma**0.5)
    print(f"la raiz cuadrada es {raiz}")
else:
    num4 = float(input("ingrese un numero: "))
    num5 = float(input("ingrese un numero: "))
    suma=suma+num4+num5
    print(f"la suma de todos los numeros es {suma}")