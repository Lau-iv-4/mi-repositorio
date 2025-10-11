 # credenciales validas (como variables individuales)
usuario_correcto = "admin"
clave_correcta = "1234"

# variable de control para el número de intentos
max_intentos = 3
intentos = 0 # Contador de intentos realizados

print("\n--- Sistema de inicio de sesión ---")

# Usamos un bucle 'while' para limitar los intentos
while intentos < max_intentos:
    
    intentos += 1 # Incrementamos el contador de intentos al inicio del ciclo
    
    print(f"\nIntentos restantes: {max_intentos - intentos + 1}") # +1 porque el contador ya aumentó
    
    # Solicitar credenciales
    print("Usuario:")
    usuario = input()
    print("Contraseña:")
    clave = input() # Corregida la sintaxis: 'clave = input()'
    
    # --- Estructuras de Control para la Validación ---
    
    # 1. Validar si algún campo está vacío (condición: 'si uno de los campos está vacío deberá mostrar un error de autentificación')
    if usuario == "" or clave == "":
        print(" ERROR DE AUTENTICACIÓN: El usuario o la contraseña no pueden estar vacíos.")
        
    # 2. Validar credenciales correctas (condición principal de éxito)
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("\n ¡Inicio de sesión exitoso! Bienvenido/a.")
        break # Salir del bucle 'while' al tener éxito
        
    # 3. Validar credenciales incorrectas (condición: 'mostrar un error al usuario cuando no exista uno de los datos')
    else:
        # Este 'else' se ejecuta si los campos no están vacíos y las credenciales son incorrectas
        print(" ERROR: Nombre de usuario o contraseña incorrectos.")

# --- Bloque de control final: Verificación de intentos agotados ---

# Este 'if' se ejecuta DESPUÉS de que el bucle 'while' termina.
# Si el bucle terminó por 'break' (éxito), 'intentos' será menor o igual a 'max_intentos'.
# Si el bucle terminó porque 'intentos' alcanzó 'max_intentos' (fracaso), se ejecuta este bloque.
if intentos == max_intentos and not (usuario == usuario_correcto and clave == clave_correcta):
    print("\n ADVERTENCIA: Has agotado tus 3 intentos. El sistema se ha bloqueado.")
