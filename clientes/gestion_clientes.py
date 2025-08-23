# Lista para almacenar clientes en memoria
clientes = [
    {
        "nombre": "Juan Pérez",
        "telefono": "956565656",
        "email": "juan.perez@email.com"
    },
    {
        "nombre": "María García",
        "telefono": "945454545",
        "email": "maria.garcia@email.com"
    },
    {
        "nombre": "Carlos López",
        "telefono": "932323232",
        "email": "carlos.lopez@email.com"
    },
    {
        "nombre": "Ana Rodríguez",
        "telefono": "987878787",
        "email": "ana.rodriguez@email.com"
    },
    {
        "nombre": "Luis Martínez",
        "telefono": "971717171",
        "email": "luis.martinez@email.com"
    },
    {
        "nombre": "Sofia Herrera",
        "telefono": "982828282",
        "email": "sofia.herrera@email.com"
    },
    {
        "nombre": "Roberto Silva",
        "telefono": "919191919",
        "email": "roberto.silva@email.com"
    },
    {
        "nombre": "Carmen Vargas",
        "telefono": "963636363",
        "email": "carmen.vargas@email.com"
    }
]

def menu_clientes():
    while True:
        print("\n--- GESTIÓN DE CLIENTES ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    
    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    clientes.append(cliente)
    print(f"Cliente {nombre} agregado exitosamente.")

def listar_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente['nombre']} - {cliente['telefono']} - {cliente['email']}")

def buscar_cliente():
    print("\n--- BUSCAR CLIENTE ---")
    nombre = input("Ingresa el nombre del cliente: ")
    
    encontrados = []
    for cliente in clientes:
        if nombre.lower() in cliente['nombre'].lower():
            encontrados.append(cliente)
    
    if encontrados:
        print("Clientes encontrados:")
        for i, cliente in enumerate(encontrados, 1):
            print(f"{i}. {cliente['nombre']} - {cliente['telefono']} - {cliente['email']}")
    else:
        print("No se encontraron clientes con ese nombre.")