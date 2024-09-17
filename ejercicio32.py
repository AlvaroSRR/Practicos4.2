sueldo=float(input("Ingrese su sueldo: "))
categoria=int(input("Ingrese numero de categoria: ").upper())
if categoria >= 1 and categoria <= 4:
    match categoria:
        case 1:
            sueldoNeto= float(sueldo*0.7)
        case 2:
            sueldoNeto= float(sueldo*0.75)
        case 3:
            sueldoNeto= float(sueldo*0.75)
        case 4:
            sueldoNeto= float(sueldo*0.9)
else:
    sueldoNeto=sueldo
    print("Su categoria no tiene descuento")
print(f"Sueldo Neto: {sueldoNeto} - Categoria {categoria}")