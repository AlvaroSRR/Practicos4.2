num=int(input("ingrese un numero entero menor a 100: "))
if num>0 and num < 100:
    control=True
    primo = 2, 3, 5, 7
    i = 0
    while control == True:
        if num == primo[i]:
            print("Numero Primo")
            control=False
        else:
            if num%primo[i] ==0:
                print("Numero no Primo")
                control=False
            else:
                i=i+1
        if i >3:
            print("Numero Primo")
            control=False
else:
    print("el numero ingresado no esta en el rango solicitado")