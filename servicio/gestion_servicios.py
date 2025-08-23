# servicios.py
from datetime import datetime

# ========================
# Datos en memoria
# ========================
servicios = []
_next_id = 1

# ========================
# Utilidades
# ========================
def format_clp(valor):
    return "$" + f"{int(valor):,}".replace(",", ".")

def input_no_vacio(prompt):
    while True:
        s = input(prompt).strip()
        if s != "":
            return s
        print("No puede estar vacío.")

def input_entero(prompt, minimo=None):
    while True:
        try:
            n = int(input(prompt))
            if minimo and n < minimo:
                raise ValueError
            return n
        except:
            print("Ingresa un número válido.")

def input_float(prompt):
    while True:
        try:
            n = float(input(prompt))
            if n < 0: raise ValueError
            return n
        except:
            print("Ingresa un número ≥ 0.")

def hoy():
    return datetime.now().strftime("%Y-%m-%d")

# ========================
# Funciones Servicios
# ========================
def registrar_servicio():
    """Item 1"""
    global _next_id
    print("\n=== Registrar Servicio ===")
    patente = input_no_vacio("Patente: ").upper()
    rut = input_no_vacio("RUT cliente: ")
    fecha = input(f"Fecha [Enter={hoy()}]: ").strip() or hoy()
    tipo = input_no_vacio("Tipo servicio: ")
    detalle = input("Detalle (opcional): ")
    mano_obra = input_float("Mano de obra: ")

    insumos = []
    print("\n--- Ingreso de insumos ---")
    while True:
        desc = input("Descripción (Enter para terminar): ").strip()
        if desc == "":
            break
        cant = input_entero("Cantidad: ", minimo=1)
        precio = input_float("Precio unitario: ")
        insumos.append({"desc": desc, "cant": cant, "precio": precio})

    subtotal = mano_obra + sum(i["cant"]*i["precio"] for i in insumos)
    iva = round(subtotal * 0.19)
    total = subtotal + iva

    servicios.append({
        "id": _next_id,
        "patente": patente,
        "rut": rut,
        "fecha": fecha,
        "tipo": tipo,
        "detalle": detalle,
        "mano_obra": mano_obra,
        "insumos": insumos,
        "subtotal": subtotal,
        "iva": iva,
        "total": total
    })
    print(f"✅ Servicio #{_next_id} registrado (Total: {format_clp(total)})")
    _next_id += 1

def listar_servicios():
    """Item 2"""
    if not servicios:
        print("\nNo hay servicios registrados.")
        return
    print("\nID  FECHA       PATENTE  RUT         TIPO               TOTAL")
    print("-"*65)
    for s in servicios:
        print(f"{s['id']:<3} {s['fecha']:<11} {s['patente']:<8} {s['rut']:<10} {s['tipo']:<18} {format_clp(s['total'])}")

def boleta_servicio():
    """Item 3"""
    if not servicios:
        print("\nNo hay servicios registrados.")
        return
    sid = input_entero("ID servicio: ", minimo=1)
    s = next((x for x in servicios if x["id"]==sid), None)
    if not s:
        print("No encontrado.")
        return

    print("\n" + "="*50)
    print(f"SERVICIO #{s['id']} — {s['fecha']}")
    print(f"Patente: {s['patente']} | Cliente: {s['rut']}")
    print(f"Tipo: {s['tipo']} — {s['detalle']}")
    print("-"*50)
    print(f"{'Concepto':<20}{'Cant.':>6}{'P.Unit':>10}{'Total':>12}")
    print("-"*50)
    print(f"{'Mano de obra':<20}{'':>6}{'':>10}{format_clp(s['mano_obra']):>12}")
    for i in s["insumos"]:
        total_i = i["cant"]*i["precio"]
        print(f"{i['desc']:<20}{i['cant']:>6}{format_clp(i['precio']):>10}{format_clp(total_i):>12}")
    print("-"*50)
    print(f"{'Subtotal':>36}{format_clp(s['subtotal']):>14}")
    print(f"{'IVA (19%)':>36}{format_clp(s['iva']):>14}")
    print(f"{'TOTAL':>36}{format_clp(s['total']):>14}")
    print("="*50)

# ========================
# Menú Servicios
# ========================
def menu_servicios():
    while True:
        print("\n=== MENÚ SERVICIOS ===")
        print("1) Registrar servicio")
        print("2) Listar servicios")
        print("3) Boleta por ID")
        print("4) Salir")
        op = input("Opción: ").strip()
        if op=="1": registrar_servicio()
        elif op=="2": listar_servicios()
        elif op=="3": boleta_servicio()
        elif op=="4": break
        else: print("Opción inválida.")

# ========================
# Main
# ========================
if __name__ == "__main__":
    print("SERVITECA — Módulo Servicios")
    menu_servicios()
