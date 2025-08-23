from autos.gestion_autos import menu_autos

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
            print("Módulo en desarrollo...")
        elif opcion == "3":
            print("Módulo en desarrollo...")
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()