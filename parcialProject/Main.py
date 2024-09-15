# Entero a cadena
num = 12
num_str = str(num)
print(num_str)  # "12"

# Cadena a entero
num_str = "22"
num = int(num_str)
print(num)  # 22

# Decimal a cadena
decimal = 3.85
decimal_str = str(decimal)
print(decimal_str)  # "3.85"

# Cadena a decimal
decimal_str = "4.659"
decimal = float(decimal_str)
print(decimal)  # 4.659

multilinea = """--- MULTILINEAS DE CADENAS Y SUBCADENAS DE PYTHON---"""
print(multilinea)

cadena = "Hola, Juan"
print(len(cadena))

cadena = "Hola, Juan"
n = 5
print(cadena[:n])

cadena = "Hola, Juan"
inicio = 4
fin = 6
print(cadena[inicio:fin])

cadena = "Hola, Juan"
n = 5
print(cadena[-n:])

cadena = "Hola, Juan"
print(cadena.upper())

cadena = "Hola, Juan"
print(cadena.lower())

multilinea = """--- MULTILINEAS DE CADENAS DE CARACTERES DE PYTHON ---"""
print(multilinea)

cadena = "   Hola, Juan   "
print(cadena.strip())

cadena = "Hola, Juan"
print(cadena.replace("Juan", "PYTHON"))

cadena = "Hola, Juan"
print(cadena.replace("Juan", "PYTHON"))

nombre = "JuanJo"
edad = 19
print(f"Me llamo {nombre} y tengo {edad} años.")