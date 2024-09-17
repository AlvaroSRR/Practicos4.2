frasco=int(input("Codigo de frascos: 1 - 2 - 3\nIngrese codigo: "))
if frasco >=1 and frasco <=3:
    match frasco:
        case 1:
            print(f"Frasco Chico")
        case 2:
            print(f"Frasco Mediano")
        case 3:
            print(f"Frasco Grande")
else:
    print(f"Codigo no Valido")