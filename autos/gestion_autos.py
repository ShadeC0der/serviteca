class Auto:
    def __init__(self, patente, modelo, color, año=None, marca=None):
        """
        Inicializa un objeto Auto con sus atributos básicos
        
        Args:
            patente (str): Patente del auto (identificador único)
            modelo (str): Modelo del auto
            color (str): Color del auto
            año (int, optional): Año del auto
            marca (str, optional): Marca del auto
        """
        self.patente = patente.upper()
        self.modelo = modelo
        self.color = color
        self.año = año
        self.marca = marca

    def __str__(self):
        """Retorna una representación en string del auto"""
        return f"Auto: {self.marca} {self.modelo} - Color: {self.color} - Patente: {self.patente} - Año: {self.año}"

    def to_dict(self):
        """Convierte el auto a un diccionario para almacenamiento"""
        return {
            'patente': self.patente,
            'modelo': self.modelo,
            'color': self.color,
            'año': self.año,
            'marca': self.marca
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un auto desde un diccionario"""
        return cls(
            patente=data['patente'],
            modelo=data['modelo'],
            color=data['color'],
            año=data.get('año'),
            marca=data.get('marca')
        )


# Datos estáticos de autos para demostración
DATOS_AUTOS_ESTATICOS = [
    {
        'patente': 'ABCD12',
        'modelo': 'Civic',
        'color': 'Rojo',
        'año': 2020,
        'marca': 'Honda'
    },
    {
        'patente': 'EFGH34',
        'modelo': 'Corolla',
        'color': 'Azul',
        'año': 2019,
        'marca': 'Toyota'
    },
    {
        'patente': 'IJKL56',
        'modelo': 'Golf',
        'color': 'Blanco',
        'año': 2021,
        'marca': 'Volkswagen'
    },
    {
        'patente': 'MNOP78',
        'modelo': 'Sentra',
        'color': 'Negro',
        'año': 2018,
        'marca': 'Nissan'
    },
    {
        'patente': 'QRST90',
        'modelo': 'Focus',
        'color': 'Gris',
        'año': 2022,
        'marca': 'Ford'
    },
    {
        'patente': 'UVWX12',
        'modelo': 'Cruze',
        'color': 'Plateado',
        'año': 2020,
        'marca': 'Chevrolet'
    },
    {
        'patente': 'YZAB34',
        'modelo': '3 Series',
        'color': 'Azul Marino',
        'año': 2021,
        'marca': 'BMW'
    },
    {
        'patente': 'CDEF56',
        'modelo': 'A3',
        'color': 'Blanco',
        'año': 2019,
        'marca': 'Audi'
    }
]


class GestionAutos:
    def __init__(self, cargar_datos_estaticos=True):
        """
        Inicializa la gestión de autos con una lista vacía
        
        Args:
            cargar_datos_estaticos (bool): Si se deben cargar datos estáticos al inicializar
        """
        self.autos = []
        if cargar_datos_estaticos:
            self.cargar_datos_estaticos()

    def cargar_datos_estaticos(self):
        """Carga los datos estáticos de autos predefinidos"""
        for auto_data in DATOS_AUTOS_ESTATICOS:
            self.agregar_auto(
                auto_data['patente'],
                auto_data['modelo'],
                auto_data['color'],
                auto_data['año'],
                auto_data['marca']
            )

    def agregar_auto(self, patente, modelo, color, año=None, marca=None):
        """
        Agrega un nuevo auto al sistema con validaciones mejoradas
        
        Args:
            patente (str): Patente del auto
            modelo (str): Modelo del auto
            color (str): Color del auto
            año (int, optional): Año del auto
            marca (str, optional): Marca del auto
            
        Returns:
            dict: Diccionario con el resultado de la operación
        """
        # Validaciones
        if not patente or not modelo or not color:
            return {
                'exito': False,
                'mensaje': 'La patente, modelo y color son obligatorios'
            }
        
        if not self.validar_patente(patente):
            return {
                'exito': False,
                'mensaje': 'Formato de patente inválido. Use formato: ABCD12 o AB1234'
            }
        
        # Verificar si la patente ya existe
        if self.buscar_por_patente(patente):
            return {
                'exito': False,
                'mensaje': f'Ya existe un auto con la patente {patente}'
            }
        
        # Validar año si se proporciona
        if año is not None:
            año_actual = 2024
            if año < 1900 or año > año_actual + 1:
                return {
                    'exito': False,
                    'mensaje': f'El año debe estar entre 1900 y {año_actual + 1}'
                }
        
        auto = Auto(patente, modelo, color, año, marca)
        self.autos.append(auto)
        
        return {
            'exito': True,
            'mensaje': f'Auto agregado exitosamente: {auto}',
            'auto': auto
        }

    def buscar_por_patente(self, patente):
        """
        Busca un auto por su patente
        
        Args:
            patente (str): Patente a buscar
            
        Returns:
            Auto: El auto encontrado o None si no existe
        """
        for auto in self.autos:
            if auto.patente == patente.upper():
                return auto
        return None

    def buscar_por_modelo(self, modelo):
        """
        Busca autos por modelo
        
        Args:
            modelo (str): Modelo a buscar
            
        Returns:
            list: Lista de autos que coinciden con el modelo
        """
        return [auto for auto in self.autos if auto.modelo.lower() == modelo.lower()]

    def buscar_por_color(self, color):
        """
        Busca autos por color
        
        Args:
            color (str): Color a buscar
            
        Returns:
            list: Lista de autos que coinciden con el color
        """
        return [auto for auto in self.autos if auto.color.lower() == color.lower()]

    def buscar_por_marca(self, marca):
        """
        Busca autos por marca
        
        Args:
            marca (str): Marca a buscar
            
        Returns:
            list: Lista de autos que coinciden con la marca
        """
        return [auto for auto in self.autos if auto.marca and auto.marca.lower() == marca.lower()]

    def modificar_auto(self, patente, **kwargs):
        """
        Modifica los datos de un auto existente
        
        Args:
            patente (str): Patente del auto a modificar
            **kwargs: Atributos a modificar (modelo, color, año, marca)
            
        Returns:
            bool: True si se modificó exitosamente, False si no se encontró
        """
        auto = self.buscar_por_patente(patente)
        if not auto:
            return False
        
        # Actualizar los atributos proporcionados
        for key, value in kwargs.items():
            if hasattr(auto, key):
                if key == 'patente':
                    setattr(auto, key, value.upper())
                else:
                    setattr(auto, key, value)
        
        return True

    def eliminar_auto(self, patente):
        """
        Elimina un auto del sistema
        
        Args:
            patente (str): Patente del auto a eliminar
            
        Returns:
            bool: True si se eliminó exitosamente, False si no se encontró
        """
        auto = self.buscar_por_patente(patente)
        if auto:
            self.autos.remove(auto)
            return True
        return False

    def listar_todos(self):
        """
        Retorna todos los autos en el sistema
        
        Returns:
            list: Lista de todos los autos
        """
        return self.autos.copy()

    def obtener_cantidad(self):
        """
        Retorna la cantidad de autos en el sistema
        
        Returns:
            int: Cantidad de autos
        """
        return len(self.autos)

    def validar_patente(self, patente):
        """
        Valida el formato de una patente (formato chileno básico)
        
        Args:
            patente (str): Patente a validar
            
        Returns:
            bool: True si el formato es válido
        """
        if not patente:
            return False
        
        patente = patente.upper().replace('-', '').replace(' ', '')
        
        # Formato básico: 4 letras + 2 números (ej: ABCD12)
        if len(patente) == 6:
            return patente[:4].isalpha() and patente[4:].isdigit()
        
        # Formato alternativo: 2 letras + 4 números (ej: AB1234)
        if len(patente) == 6:
            return patente[:2].isalpha() and patente[2:].isdigit()
        
        return False

    def exportar_a_lista(self):
        """
        Exporta todos los autos a una lista de diccionarios
        
        Returns:
            list: Lista de diccionarios con los datos de los autos
        """
        return [auto.to_dict() for auto in self.autos]

    def importar_desde_lista(self, lista_autos):
        """
        Importa autos desde una lista de diccionarios
        
        Args:
            lista_autos (list): Lista de diccionarios con datos de autos
        """
        for auto_data in lista_autos:
            if isinstance(auto_data, dict) and 'patente' in auto_data:
                # Verificar que no exista ya
                if not self.buscar_por_patente(auto_data['patente']):
                    auto = Auto.from_dict(auto_data)
                    self.autos.append(auto)

    def listar_autos(self, formato='completo'):
        """
        Lista todos los autos con formato mejorado
        
        Args:
            formato (str): Formato de salida ('completo', 'resumido', 'tabla')
            
        Returns:
            str: Lista formateada de autos
        """
        if not self.autos:
            return "No hay autos registrados en el sistema."
        
        if formato == 'resumido':
            resultado = f"Total de autos: {len(self.autos)}\n"
            for i, auto in enumerate(self.autos, 1):
                resultado += f"{i}. {auto.marca} {auto.modelo} - {auto.patente} ({auto.color})\n"
        
        elif formato == 'tabla':
            resultado = f"{'N°':<3} {'Patente':<8} {'Marca':<12} {'Modelo':<12} {'Color':<10} {'Año':<6}\n"
            resultado += "-" * 60 + "\n"
            for i, auto in enumerate(self.autos, 1):
                resultado += f"{i:<3} {auto.patente:<8} {(auto.marca or 'N/A'):<12} {auto.modelo:<12} {auto.color:<10} {(str(auto.año) if auto.año else 'N/A'):<6}\n"
        
        else:  # formato completo
            resultado = f"=== LISTADO DE AUTOS ({len(self.autos)} total) ===\n"
            for i, auto in enumerate(self.autos, 1):
                resultado += f"\n{i}. {auto}\n"
        
        return resultado

    def buscar_auto(self, criterio, valor):
        """
        Busca autos por diferentes criterios con resultados formateados
        
        Args:
            criterio (str): Criterio de búsqueda ('patente', 'modelo', 'color', 'marca', 'año')
            valor: Valor a buscar
            
        Returns:
            str: Resultados de la búsqueda formateados
        """
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
        elif criterio == 'año':
            try:
                año = int(valor)
                resultados = [auto for auto in self.autos if auto.año == año]
            except ValueError:
                return "Error: El año debe ser un número válido"
        else:
            return f"Error: Criterio '{criterio}' no válido. Use: patente, modelo, color, marca, año"
        
        if not resultados:
            return f"No se encontraron autos con {criterio}: '{valor}'"
        
        # Formatear resultados
        resultado = f"=== RESULTADOS DE BÚSQUEDA ({len(resultados)} encontrados) ===\n"
        resultado += f"Criterio: {criterio.upper()} = '{valor}'\n\n"
        
        for i, auto in enumerate(resultados, 1):
            resultado += f"{i}. {auto}\n"
        
        return resultado

    def buscar_auto_interactivo(self):
        """
        Función interactiva para buscar autos con menú de opciones
        
        Returns:
            str: Resultado de la búsqueda
        """
        print("\n=== BÚSQUEDA DE AUTOS ===")
        print("1. Buscar por patente")
        print("2. Buscar por modelo")
        print("3. Buscar por color")
        print("4. Buscar por marca")
        print("5. Buscar por año")
        print("0. Volver")
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "0":
                return "Búsqueda cancelada"
            
            criterios = {
                "1": "patente",
                "2": "modelo", 
                "3": "color",
                "4": "marca",
                "5": "año"
            }
            
            if opcion not in criterios:
                return "Opción inválida"
            
            criterio = criterios[opcion]
            valor = input(f"Ingrese el {criterio} a buscar: ").strip()
            
            if not valor:
                return "Valor de búsqueda no puede estar vacío"
            
            return self.buscar_auto(criterio, valor)
            
        except KeyboardInterrupt:
            return "Búsqueda cancelada por el usuario"


# Función de ejemplo para demostrar el uso
def ejemplo_uso():
    """Función de ejemplo que muestra cómo usar la gestión de autos"""
    print("=== DEMOSTRACIÓN DE GESTIÓN DE AUTOS ===")
    
    # Inicializar con datos estáticos
    gestion = GestionAutos(cargar_datos_estaticos=True)
    print(f"Se cargaron {gestion.obtener_cantidad()} autos desde datos estáticos")
    
    # 1. DEMOSTRAR AGREGAR AUTO
    print("\n" + "="*50)
    print("1. FUNCIÓN AGREGAR AUTO")
    print("="*50)
    
    # Agregar auto exitosamente
    resultado = gestion.agregar_auto("XYZ789", "Swift", "Verde", 2023, "Suzuki")
    print(f"Resultado: {resultado['mensaje']}")
    
    # Intentar agregar auto con patente duplicada
    resultado = gestion.agregar_auto("ABCD12", "Otro", "Negro", 2024, "Marca")
    print(f"Resultado: {resultado['mensaje']}")
    
    # Intentar agregar auto con patente inválida
    resultado = gestion.agregar_auto("123", "Modelo", "Rojo", 2024, "Marca")
    print(f"Resultado: {resultado['mensaje']}")
    
    # 2. DEMOSTRAR LISTAR AUTOS
    print("\n" + "="*50)
    print("2. FUNCIÓN LISTAR AUTOS")
    print("="*50)
    
    print("\nFormato completo:")
    print(gestion.listar_autos('completo'))
    
    print("\nFormato resumido:")
    print(gestion.listar_autos('resumido'))
    
    print("\nFormato tabla:")
    print(gestion.listar_autos('tabla'))
    
    # 3. DEMOSTRAR BUSCAR AUTO
    print("\n" + "="*50)
    print("3. FUNCIÓN BUSCAR AUTO")
    print("="*50)
    
    # Buscar por patente
    print("\nBúsqueda por patente:")
    print(gestion.buscar_auto('patente', 'ABCD12'))
    
    # Buscar por modelo
    print("\nBúsqueda por modelo:")
    print(gestion.buscar_auto('modelo', 'Civic'))
    
    # Buscar por color
    print("\nBúsqueda por color:")
    print(gestion.buscar_auto('color', 'Blanco'))
    
    # Buscar por marca
    print("\nBúsqueda por marca:")
    print(gestion.buscar_auto('marca', 'Honda'))
    
    # Buscar por año
    print("\nBúsqueda por año:")
    print(gestion.buscar_auto('año', '2020'))
    
    # Búsqueda que no encuentra resultados
    print("\nBúsqueda sin resultados:")
    print(gestion.buscar_auto('patente', 'NOEXISTE'))
    
    print("\n" + "="*50)
    print("DEMOSTRACIÓN COMPLETADA")
    print("="*50)


def menu_interactivo():
    """Menú interactivo para probar todas las funcionalidades de gestión de autos"""
    gestion = GestionAutos(cargar_datos_estaticos=True)
    
    while True:
        print("\n" + "="*60)
        print("           GESTIÓN DE AUTOS - MENÚ PRINCIPAL")
        print("="*60)
        print("1. Agregar auto")
        print("2. Listar autos")
        print("3. Buscar auto")
        print("4. Modificar auto")
        print("5. Eliminar auto")
        print("6. Ver estadísticas")
        print("7. Ejecutar demostración completa")
        print("0. Salir")
        print("="*60)
        
        try:
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
                print(f"\nResultado: {resultado['mensaje']}")
                
            elif opcion == "2":
                print("\n--- LISTAR AUTOS ---")
                print("1. Formato completo")
                print("2. Formato resumido")
                print("3. Formato tabla")
                formato_opcion = input("Seleccione formato: ").strip()
                
                formatos = {"1": "completo", "2": "resumido", "3": "tabla"}
                formato = formatos.get(formato_opcion, "completo")
                
                print(f"\n{gestion.listar_autos(formato)}")
                
            elif opcion == "3":
                resultado = gestion.buscar_auto_interactivo()
                print(f"\n{resultado}")
                
            elif opcion == "4":
                print("\n--- MODIFICAR AUTO ---")
                patente = input("Patente del auto a modificar: ").strip()
                print("Deje vacío para no modificar:")
                modelo = input("Nuevo modelo: ").strip()
                color = input("Nuevo color: ").strip()
                año_str = input("Nuevo año: ").strip()
                marca = input("Nueva marca: ").strip()
                
                kwargs = {}
                if modelo: kwargs['modelo'] = modelo
                if color: kwargs['color'] = color
                if año_str: kwargs['año'] = int(año_str)
                if marca: kwargs['marca'] = marca
                
                if gestion.modificar_auto(patente, **kwargs):
                    print("Auto modificado exitosamente")
                else:
                    print("No se encontró el auto con esa patente")
                    
            elif opcion == "5":
                print("\n--- ELIMINAR AUTO ---")
                patente = input("Patente del auto a eliminar: ").strip()
                if gestion.eliminar_auto(patente):
                    print("Auto eliminado exitosamente")
                else:
                    print("No se encontró el auto con esa patente")
                    
            elif opcion == "6":
                print("\n--- ESTADÍSTICAS ---")
                print(f"Total de autos: {gestion.obtener_cantidad()}")
                
                if gestion.autos:
                    # Estadísticas por marca
                    marcas = {}
                    colores = {}
                    años = {}
                    
                    for auto in gestion.autos:
                        # Contar marcas
                        marca = auto.marca or "Sin marca"
                        marcas[marca] = marcas.get(marca, 0) + 1
                        
                        # Contar colores
                        colores[auto.color] = colores.get(auto.color, 0) + 1
                        
                        # Contar años
                        if auto.año:
                            años[auto.año] = años.get(auto.año, 0) + 1
                    
                    print(f"\nMarcas más comunes:")
                    for marca, cantidad in sorted(marcas.items(), key=lambda x: x[1], reverse=True):
                        print(f"  {marca}: {cantidad}")
                    
                    print(f"\nColores más comunes:")
                    for color, cantidad in sorted(colores.items(), key=lambda x: x[1], reverse=True):
                        print(f"  {color}: {cantidad}")
                    
                    if años:
                        print(f"\nAños de fabricación:")
                        for año, cantidad in sorted(años.items()):
                            print(f"  {año}: {cantidad}")
                
            elif opcion == "7":
                ejemplo_uso()
                
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except ValueError as e:
            print(f"Error de entrada: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    # Descomentar la línea que desees usar:
    # ejemplo_uso()  # Para ver la demostración automática
    menu_interactivo()  # Para usar el menú interactivo
