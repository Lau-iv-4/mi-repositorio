# Proceso Cajero Automático GRLI - 

# variables para contar billetes 
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 =10
billetes_20 =10

# variables para billetes a entregar 
billetes_1000 = 0
billetes_500 = 0
billetes_200 = 0
billetes_100 = 0
billetes_50 = 0
billetes_20 = 0

# iniciamos el sistema 
print("\n--- CAJERO AUTOMÁTICO GRLI ---")

# Solicitar monto
print = ("\nIngrese el monto a retirar: ")
entrada = input ()

#trasnsformamos el valor dato a un tipo de dato entero 
monto = int(entrada)  

# Validaciones iniciales
if montoRetirar <= 0:
    print("Error: El monto a retirar debe ser mayor a cero.")
elif montoRetirar % 10 != 0:
    print("Error: El monto debe ser múltiplo de 10.")
else:
    print("\nProcesando su retiro...\n")

    # Inicializar contadores
    c_billetes1000 = 0
    c_billetes500 = 0
    c_billetes200 = 0
    c_billetes100 = 0

    montoActualizado = montoRetirar

    # Calcular billetes de 100
    while montoActualizado >= 1000 and billetes1000 > 0:
        c_billetes100 += 1
        montoActualizado -= 1000
        billetes100 -= 1

    # Calcular billetes de 50
    while montoActualizado >= 500 and billetes500 > 0:
        c_billetes50 += 1
        montoActualizado -= 500
        billetes50 -= 1

    # Calcular billetes de 200
    while montoActualizado >= 20 and billetes200 > 0:
        c_billetes20 += 1
        montoActualizado -= 200
        billetes20 -= 1

    # Calcular billetes de 100
    while montoActualizado >= 10 and billetes100 > 0:
        c_billetes10 += 1
        montoActualizado -= 100
        billetes10 -= 1

    # Verificar si se completó el retiro
    if montoActualizado == 0:
        print("\n¡Retiro exitoso!")
        print("\nSe han dispensado los siguientes billetes:")
        if c_billetes100 > 0:
            print(f"{c_billetes100} billetes de $100")
        if c_billetes50 > 0:
            print(f"{c_billetes50} billetes de $50")
        if c_billetes20 > 0:
            print(f"{c_billetes20} billetes de $20")
        if c_billetes10 > 0:
            print(f"{c_billetes10} billetes de $10")
    else:
        print("Error: No hay billetes suficientes.")
        print("Por favor, intente con otro monto.")

# Mensaje final
print("\n ¡GRACIAS POR USAR EL CAJERO!")
input("Presione enter para finalizar...")

