class Auto:
    def __init__(self, patente, modelo, color, año=None, marca=None):
        self.patente = patente.upper()
        self.modelo = modelo
        self.color = color
        self.año = año
        self.marca = marca

    def __str__(self):
        return f"Auto: {self.marca} {self.modelo} - Color: {self.color} - Patente: {self.patente} - Año: {self.año}"

    def to_dict(self):
        return {
            'patente': self.patente,
            'modelo': self.modelo,
            'color': self.color,
            'año': self.año,
            'marca': self.marca
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            patente=data['patente'],
            modelo=data['modelo'],
            color=data['color'],
            año=data.get('año'),
            marca=data.get('marca')
        )


# Datos de ejemplo
DATOS_AUTOS = [
    {'patente': 'ABCD12', 'modelo': 'Civic', 'color': 'Rojo', 'año': 2020, 'marca': 'Honda'},
    {'patente': 'EFGH34', 'modelo': 'Corolla', 'color': 'Azul', 'año': 2019, 'marca': 'Toyota'},
    {'patente': 'IJKL56', 'modelo': 'Golf', 'color': 'Blanco', 'año': 2021, 'marca': 'Volkswagen'}
]


class GestionAutos:
    def __init__(self):
        self.autos = []
        self.cargar_datos_ejemplo()

    def cargar_datos_ejemplo(self):
        for auto_data in DATOS_AUTOS:
            self.agregar_auto(
                auto_data['patente'],
                auto_data['modelo'],
                auto_data['color'],
                auto_data['año'],
                auto_data['marca']
            )

    def agregar_auto(self, patente, modelo, color, año=None, marca=None):
        if not patente or not modelo or not color:
            return {'exito': False, 'mensaje': 'La patente, modelo y color son obligatorios'}
        
        if self.buscar_por_patente(patente):
            return {'exito': False, 'mensaje': f'Ya existe un auto con la patente {patente}'}
        
        auto = Auto(patente, modelo, color, año, marca)
        self.autos.append(auto)
        return {'exito': True, 'mensaje': f'Auto agregado: {auto}'}

    def buscar_por_patente(self, patente):
        for auto in self.autos:
            if auto.patente == patente.upper():
                return auto
        return None

    def buscar_por_modelo(self, modelo):
        return [auto for auto in self.autos if auto.modelo.lower() == modelo.lower()]

    def buscar_por_color(self, color):
        return [auto for auto in self.autos if auto.color.lower() == color.lower()]

    def buscar_por_marca(self, marca):
        return [auto for auto in self.autos if auto.marca and auto.marca.lower() == marca.lower()]

    def modificar_auto(self, patente, **kwargs):
        auto = self.buscar_por_patente(patente)
        if not auto:
            return False
        
        for key, value in kwargs.items():
            if hasattr(auto, key):
                setattr(auto, key, value)
        return True

    def eliminar_auto(self, patente):
        auto = self.buscar_por_patente(patente)
        if auto:
            self.autos.remove(auto)
            return True
        return False

    def listar_todos(self):
        return self.autos.copy()

    def obtener_cantidad(self):
        return len(self.autos)

    def listar_autos(self):
        if not self.autos:
            return "No hay autos registrados."
        
        resultado = f"=== LISTADO DE AUTOS ({len(self.autos)} total) ===\n"
        for i, auto in enumerate(self.autos, 1):
            resultado += f"{i}. {auto}\n"
        return resultado

    def buscar_auto(self, criterio, valor):
        resultados = []
        
        if criterio == 'patente':
            auto = self.buscar_por_patente(valor)
            if auto:
                resultados = [auto]
        elif criterio == 'modelo':
            resultados = self.buscar_por_modelo(valor)
        elif criterio == 'color':
            resultados = self.buscar_por_color(valor)
        elif criterio == 'marca':
            resultados = self.buscar_por_marca(valor)
        else:
            return f"Error: Criterio '{criterio}' no válido"
        
        if not resultados:
            return f"No se encontraron autos con {criterio}: '{valor}'"
        
        resultado = f"=== RESULTADOS ({len(resultados)} encontrados) ===\n"
        for i, auto in enumerate(resultados, 1):
            resultado += f"{i}. {auto}\n"
        return resultado


def menu_principal():
    gestion = GestionAutos()
    
    while True:
        print("\n=== GESTIÓN DE AUTOS ===")
        print("1. Agregar auto")
        print("2. Listar autos")
        print("3. Buscar auto")
        print("4. Modificar auto")
        print("5. Eliminar auto")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
            
        elif opcion == "1":
            print("\n--- AGREGAR AUTO ---")
            patente = input("Patente: ").strip()
            modelo = input("Modelo: ").strip()
            color = input("Color: ").strip()
            año_str = input("Año (opcional): ").strip()
            marca = input("Marca (opcional): ").strip()
            
            año = int(año_str) if año_str else None
            resultado = gestion.agregar_auto(patente, modelo, color, año, marca)
            print(f"Resultado: {resultado['mensaje']}")
            
        elif opcion == "2":
            print(gestion.listar_autos())
            
        elif opcion == "3":
            print("\n--- BUSCAR AUTO ---")
            print("1. Por patente")
            print("2. Por modelo")
            print("3. Por color")
            print("4. Por marca")
            
            sub_opcion = input("Seleccione criterio: ").strip()
            criterios = {"1": "patente", "2": "modelo", "3": "color", "4": "marca"}
            
            if sub_opcion in criterios:
                valor = input(f"Ingrese {criterios[sub_opcion]}: ").strip()
                print(gestion.buscar_auto(criterios[sub_opcion], valor))
            else:
                print("Opción inválida")
                
        elif opcion == "4":
            print("\n--- MODIFICAR AUTO ---")
            patente = input("Patente del auto: ").strip()
            modelo = input("Nuevo modelo (vacío para no cambiar): ").strip()
            color = input("Nuevo color (vacío para no cambiar): ").strip()
            
            kwargs = {}
            if modelo: kwargs['modelo'] = modelo
            if color: kwargs['color'] = color
            
            if gestion.modificar_auto(patente, **kwargs):
                print("Auto modificado exitosamente")
            else:
                print("No se encontró el auto")
                
        elif opcion == "5":
            print("\n--- ELIMINAR AUTO ---")
            patente = input("Patente del auto: ").strip()
            if gestion.eliminar_auto(patente):
                print("Auto eliminado exitosamente")
            else:
                print("No se encontró el auto")
                
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu_principal()
