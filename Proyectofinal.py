p = str(input("Ingrese el producto: "))
new_cantidad=float(input("Ingrese la cantidad: "))
clave=str(input("Ingrese clave de comprador: "))
def pu():
    if p == "P1":
        return 234
    elif p == "P2":
        return 265
    if p == "P3":
        return 278
    elif p == "P4":
        return 299
    if p == "P5":
        return 334
    elif p == "P6":
        return 365
    else:
        print("Error")
def dsct(new_cantidad,p):
    if new_cantidad >= 1000:
        return new_cantidad*0.90*pu()
    elif new_cantidad >= 100 and new_cantidad < 1000:
        return new_cantidad*0.93*pu()
    elif new_cantidad >= 50 and new_cantidad < 100:
        return new_cantidad * 0.98*pu()
    elif new_cantidad > 0 and new_cantidad < 50:
        return new_cantidad*pu()
def obsequio(clave):
    if clave == "CF1":
        return 50
    elif clave == "CF2":
        return 30
    elif clave == "CF3":
        return 10
    else:
        return 0
print("El precio final es de: ", dsct(new_cantidad, p), " y su obsequio es :", obsequio)


