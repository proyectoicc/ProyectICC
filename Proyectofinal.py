print("¿Qué desea realizar? \nPresione:")
print("    1 : Calcular el precio y obsequio \n    2 : Agregar un nuevo valor  \n    3 : Otros")

precios={"P1" : 23.4, "P2" : 26.5, "P3" : 27.8, "P4" : 29.9, "P5" : 33.4, "P6" : 36.5}

#FUNCIONES
def Precio(precios,p):
    for i in precios:
        if i == p:
            return (precios[p])

def pfinal(cantidad_compra, x):
    if cantidad_compra >= 1000:
        return (cantidad_compra*0.90*x)
    elif cantidad_compra >= 100 and cantidad_compra < 1000:
        return (cantidad_compra*0.93*x)
    elif cantidad_compra >= 50 and cantidad_compra < 100:
        return (cantidad_compra * 0.98*x)
    elif cantidad_compra > 0 and cantidad_compra < 50:
        return (cantidad_compra * x)

def obsequio(clave):
    if clave == "CF1":
        return 5
    elif clave == "CF2":
        return 3
    elif clave == "CF3":
        return 1
    else:
        return 0

def Add_value():

    print("Ingrese el código del nuevo producto: ")
    new_data = str(input())
    print("Ingrese el precio unitario del nuevo producto: ")
    value_new_data = float(input())
    precios.update({new_data: value_new_data})

    print(archivo.read())
    print("¡Valor añadido!")

def Otro(precios):
    print("Presione:\n   1 : Cambiar el código de un producto \n   2 : Cambiar el precio de un producto \n   3 : Mostrar precios" )
    r = int(input())

    if r == 1:
        print("Ingrese el código a reemplazar:")
        code_replace = str(input())
        for i in precios:
            if code_replace == i :
                old_value = precios[i]
                del precios [code_replace]
                print("Ingrese el nuevo código:")
                new_code = str(input())
                precios.update({new_code : old_value})
                print("¡Valor reemplazado!")
                break

    elif r == 2:
        print("Ingrese el código del valor a reemplazar:")
        code_replace = str(input())
        for i in precios:
            if code_replace == i :
                old_code = i
                del precios [code_replace]
                print("Ingrese el nuevo precio por unidad del producto:")
                new_value = float(input())
                precios.update({old_code : new_value})
                print("¡Valor reemplazado!")
                break

    elif r == 3:
        print(precios)

action=int(input())

#INICIO DEL PROGRAMA
if action == 1:
    cantidad_compra=float(input("Ingrese la cantidad: "))
    clave=str(input("Ingrese clave de comprador: "))
    p = str(input("Ingrese el código del producto: "))
    R=Precio(precios,p)
    print(R)
    pfinal(cantidad_compra,R)
    obsequio(clave)
    #Usar un while para poder pedir mas valores
    print("El precio final es: ", pfinal(cantidad_compra,R), "el obsequio es:", obsequio(clave))

elif action == 2:
    Add_value()

elif action == 3:
    Otro(precios)
