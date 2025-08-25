from autos.gestion_autos import menu_autos
from clientes.gestion_clientes import menu_clientes
from servicios.gestion_servicios import menu_servicios

def menu_principal():
    while True:
        print("\n--- SERVITECA ---")
        print("1. Gestionar autos")
        print("2. Gestionar clientes")
        print("3. Gestionar servicios")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            menu_autos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_servicios()
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()