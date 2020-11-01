""" Menú del programa """
import os
import helpers
import manager


def loop():

    while True:

        helpers.clear()  # 'clear' para Linux y OS X

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")

        os.system('cls')  # 'clear' para Linux y OS X

        if option == '1':
            print("Listando los clientes...\n")
            manager.show_all()
        if option == '2':
            print("Mostrando un cliente...\n")
            
        if option == '3':
            print("Modificando un cliente...\n")
            
        if option == '4':
            print("Modificando un cliente...\n")
            
        if option == '5':
            print("Borrando un cliente...\n")
            
        if option == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")