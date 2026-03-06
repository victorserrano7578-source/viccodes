class persona_cine:
    def __init__(self, idp, n, c):
        self.id = idp
        self.nom = n
        self.correo = c

class userCine(persona_cine):
    def __init__(self, idp, n, c, pts_fidel):
        self.id = idp
        self.nom = n
        self.correo = c
        self.pts = pts_fidel

class unLugar:
    def __init__(self, i, n):
        self.id_lug = i
        self.nombre_lug = n

class salaCine(unLugar):
    def __init__(self, i, n, t):
        self.id_lug = i
        self.nombre_lug = n
        self.tipo_sala = t
        self.ocupados = ["A2"]
        self.ids_reservas = ["88"]

class tiendita:
    def __init__(self):
        self.cosas = []
        self.cosas.append([1, "Palomitas Grandes", 85.0, "Snacks"])
        self.cosas.append([2, "Refresco Mediano", 45.0, "Bebidas"])
        self.cosas.append([3, "Hot Dog", 60.0, "Comida"])
        self.cosas.append([4, "Nachos con Queso", 70.0, "snacks"])
        self.cosas.append([5, "Chocolate Crunch", 35.0, "Dulces"])
        self.cosas.append([6, "Agua Ciel 600ml", 30.0, "Bebidas"])
        self.cosas.append([7, "Combo Pareja", 210.0, "Combos"])
        self.cosas.append([8, "Entrada 2D Adulto", 80.0, "Boletos"])
        self.cosas.append([9, "Entrada 3D Niño", 65.0, "Boletos"])
        self.cosas.append([10, "Cubeta Promocional", 150.0, "Promos"])

mitienda = tiendita()
usr = userCine(1, "Victor", "Victor@mail.com", 150)
sala_4 = salaCine(4, "Sala 04", "IMAX")

print("<<< REGISTRADORA Vic (10 OBJETOS) >>>")
for cosita in mitienda.cosas:
    num = str(cosita[0])
    if cosita[0] < 10:
        num = num + " "
    
    precioFinal = str(cosita[2]) + "0"
    print("ID: " + num + " | " + cosita[1] + " ($" + precioFinal + ") - Cat: " + cosita[3])

print("\n<<< VALIDACION COMPLETADA >>>\n")

print("<<< INICIANDO PROCESO DE RESERVA >>>")
print("Usuario: " + usr.nom + " (Puntos: " + str(usr.pts) + ")")
print("Pelicula: 'Rapidos y Furiosos 5 ' | Sala: 0" + str(sala_4.id_lug) + " (" + sala_4.tipo_sala + ")")



precio_boleto = 150.0
corriendo = 1

while corriendo == 1:
    entrada = input("Seleccione sus asientos (separados por coma): ")
    pedazos = entrada.split(',')
    
    asientos_buenos = []
    for p in pedazos:
        asientos_buenos.append(p.strip())
        
    print("\n[SISTEMA]: <<< Verificando disponibilidad >>>")
    
    bad_asiento = ""
    bad_reserva = ""
    huboError = 0
    
    for ast in asientos_buenos:
        if ast in sala_4.ocupados:
            huboError = 1
            bad_asiento = ast
            idx = sala_4.ocupados.index(ast)
            bad_reserva = sala_4.ids_reservas[idx]
            break
            
    if huboError == 1:
        print("[ERROR]: El asiento " + bad_asiento + " ya esta ocupado  #" + bad_reserva + ".")
        print("[SISTEMA]: seleccione asientos disponibles.\n")
    else:
        total = precio_boleto * len(asientos_buenos)
        
        juntos = ""
        for a in asientos_buenos:
            juntos = juntos + a + ", "
            
        juntos = juntos[:-2]
        
        print("[OK]: Asientos " + juntos + " bloqueados con exito.")
        print("Monto base: $" + str(total) + "0")
        
        corriendo = 0