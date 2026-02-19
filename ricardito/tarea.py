import os
os.system("cls")    

def  registro_pedido(nombre= "invitado",**datos): 
    nombre= input("Ingrese su nombre: ")
    telefono= input("Ingrese su numero de telefono: ")
    direccion= input("Ingrese su direccion: ")
    pedido= input("Ingrese su pedido: ")

    return print( f"Nombre: {nombre}\nTelefono: {telefono}\nDireccion: {direccion}\nPedido: {pedido}")

registro_pedido() 