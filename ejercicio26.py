num=int(input("ingrese un numero entero menor a 100: "))
txtprimo="el numero es primo "
#funcion
"""funcion
def calcularprimo(num):
    while primo < 100:
        if num != primo:
            primo = primo + i
        else:
            txtprimo("no es numero primo")
            primo = 100
    return
"""
if num>0:
    if num < 100:
        #control
        primo = 2
        i=2
        while primo < 100:
            if num != primo:
                primo=primo+i
            else:
                txtprimo("no es numero primo")
                primo = 100
        primo=3
        i=3
        while primo < 100:
            if num != primo:
                primo=primo+i
            else:
                txtprimo=("no es numero primo")
                primo = 100
        primo=5
        i=5
        while primo < 100:
            if num != primo:
                primo=primo+i
            else:
                txtprimo=("no es numero primo")
                primo=100
        primo=7
        i=7
        while primo < 100:
            if num != primo:
                primo=primo+i
            else:
                txtprimo=("no es numero primo")
                primo = 100
        if primo >=100:
            print(txtprimo)
    else:
        print("el numero ingresado no esta en el rango solicitado")
else:
    print("el numero ingresado no esta en el rango solicitado")