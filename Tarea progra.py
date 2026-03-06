from abc import ABC

class Persona(ABC):
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo

class Cliente(Persona):
    def __init__(self, id, nombre, correo, puntos=0):
        super().__init__(id, nombre, correo)
        self.puntos = puntos
        self.compras = []

class Staff(Persona):
    def __init__(self, id, nombre, correo, rol, turno):
        super().__init__(id, nombre, correo)
        self.rol = rol
        self.turno = turno

class Lugar:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Sala(Lugar):
    def __init__(self, id, nombre, tipo, asientos_max):
        super().__init__(id, nombre)
        self.tipo = tipo
        self.asientos_max = asientos_max
        self.asientos_ocupados = {}

class Tienda(Lugar):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.inventario = [] 

    def cargar_inventario(self):
        self.inventario = [
            (1, "Palomitas Grandes", 85.0, "Snacks"),
            (2, "Refresco Mediano", 45.0, "Bebidas"),
            (3, "Hot Dog", 60.0, "Comida"),
            (4, "Nachos con Queso", 70.0, "Snacks"),
            (5, "Chocolate Crunch", 35.0, "Dulces"),
            (6, "Agua Ciel 600ml", 30.0, "Bebidas"),
            (7, "Combo Pareja", 210.0, "Combos"),
            (8, "Entrada 2D Adulto", 80.0, "Boletos"),
            (9, "Entrada 3D Niño", 65.0, "Boletos"),
            (10, "Cubeta Promocional", 150.0, "Promos")
        ]

    def mostrar_inventario(self):
        print("--- REGISTRO MANUAL DE INVENTARIO (10 OBJETOS) ---")
        for id_prod, nombre, precio, categoria in self.inventario:
            print(f"ID: {id_prod:<2} | {nombre} (${precio:.1f}) - Cat: {categoria}")
        print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---\n")

class Peli:
    def __init__(self, titulo, minutos, edad):
        self.titulo = titulo
        self.minutos = minutos
        self.edad = edad 

class Show:
    def __init__(self, id, peli, sala, hora, precio):
        self.id = id
        self.peli = peli
        self.sala = sala
        self.hora = hora
        self.precio = precio

class Promo:
    def __init__(self, codigo, descuento):
        self.codigo = codigo
        self.descuento = descuento 

class Ticket:
    def __init__(self, id, cliente, show, asientos):
        self.id = id
        self.cliente = cliente
        self.show = show
        self.asientos = asientos
        self.total = show.precio * len(asientos)
        self.pagado = False

def main():
    dulceria = Tienda(1, "Dulcería Principal")
    dulceria.cargar_inventario()

    usuario = Cliente(1, "Carlos88", "carlos@mail.com", puntos=150)
    
    sala_imax = Sala(4, "Sala 04", "IMAX", 150)
    sala_imax.asientos_ocupados = {"A2": "882"} 
    
    pelicula = Peli("Dune: Part Two", 166, "B")
    funcion = Show(1, pelicula, sala_imax, "20:00", 150.00)

    dulceria.mostrar_inventario()

    print(">>> INICIANDO LA RESERVA...")
    print(f"Usuario: {usuario.nombre} (Puntos: {usuario.puntos})")
    print(f"Película: '{funcion.peli.titulo}' | Sala: 0{funcion.sala.id} ({funcion.sala.tipo})")

    while True:
        entrada = input("Seleccione sus asientos (separados por coma): ")
        asientos_elegidos = [asiento.strip() for asiento in entrada.split(',')]
        
        print("\n[SISTEMA]: Verificando disponibilidad...")
        
        asiento_con_error = None
        id_reserva_previa = None
        
        for asiento in asientos_elegidos:
            if asiento in funcion.sala.asientos_ocupados:
                asiento_con_error = asiento
                id_reserva_previa = funcion.sala.asientos_ocupados[asiento]
                break
                
        if asiento_con_error:
            print(f"[ERROR]: El asiento {asiento_con_error} ya está ocupado por la Reserva #{id_reserva_previa}.")
            print("[SISTEMA]:  seleccione asientos disponibles.\n")
        else:
            mi_ticket = Ticket(883, usuario, funcion, asientos_elegidos)
            asientos_texto = ", ".join(mi_ticket.asientos)
            
            print(f"[OK]: Asientos {asientos_texto} bloqueados con éxito.")
            print(f"Monto base: ${mi_ticket.total:.2f}")
            
            for a in mi_ticket.asientos:
                funcion.sala.asientos_ocupados[a] = mi_ticket.id
                
            break

if __name__ == "__main__":
    main()