num1=float(input("ingrese un numero: "))
num2=float(input("ingrese un numero negativo: "))
num3=float(input("ingrese un numero: "))
raiz=float
if num2 <0:
    raiz=(num1+num3)**0.5
    print(f"la raiz cuadrada de la suma de los numeros {num1} y {num3} es {raiz}")
else:
    print("el segundo numero ingresado no es negativo")