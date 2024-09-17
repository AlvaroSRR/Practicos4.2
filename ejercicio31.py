numCondicion=int(input("Ingrese un numero entero: "))
try:
    if numCondicion >=1 and numCondicion <= 4:
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero: "))
        match numCondicion:
            case 1:
                resultado= float(num1+num2)
            case 2:
                resultado=float(num1*num2)
            case 3:
                resultado=float(num1/num2)
            case 4:
                resultado=float(((num1**2)+(num2**2))**0.5)
    else:
        raise print("Primer numero ingresado fuera de rango")
    print(f"resultado: {resultado}")
finally:()