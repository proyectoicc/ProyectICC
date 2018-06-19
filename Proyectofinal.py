p = str(input("Ingrese el producto: "))
cantidad_compra=float(input("Ingrese la cantidad: "))
clave=str(input("Ingrese clave de comprador: "))
def pu():
    if p == "P1":
        return 23.4
    elif p == "P2":
        return 26.5
    if p == "P3":
        return 27.8
    elif p == "P4":
        return 29.9
    if p == "P5":
        return 33.4
    elif p == "P6":
        return 36.5
    else:
        print("Error")
def pfinal(cantidad_compra,p):
    if cantidad_compra >= 1000:
        return cantidad_compra*0.90*pu()
    elif cantidad_compra >= 100 and cantidad_compra < 1000:
        return cantidad*0.93*pu()
    elif cantidad >= 50 and cantidad < 100:
        return cantidad * 0.98*pu()
    elif cantidad > 0 and cantidad < 50:
        return cantidad*pu()
def obsequio(clave):
    if clave == "CF1":
        return 5
    elif clave == "CF2":
        return 3
    elif clave == "CF3":
        return 1
    else:
        return 0
print("El precio final es de: ", pfinal(new_cantidad, p), " y su obsequio es :", obsequio)
