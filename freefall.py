"""
Calcular la posición final (y) en caida libre.
y0 = altura inicial (metros) - altura_inicial
v0 = velocidad inicial ( metros/segundos) - velocidad_inicial (por defecto 0)
t = Tiempo (segundos) - tiempo
g = Aceleración de la gravedad (por defecto 9.8m/s2) - GRAVEDAD

y = y0 + ( v0 * t) + ( 0.5 * g * t**2)
Return:
    la altura actual en metros - altura_actual
La formula de la velocidad final es: Vf = g t


"""

print("Vamos a calcular la altura a la que termina un objeto que cae en caída libre, dame los datos en SI fokin imperialista :) ")
# Inicializar constantes

#La de gravedad es un diccionario del que puedes escoger el planeta y éste ya tiene su gravedad asignada.
GRAVEDADES = {
    "tierra": 9.81,
    "marte": 3.7,
    "luna": 1.62,
    "sol":274,
    "jupiter":24.79,
}
VELOCIDAD_INICIAL = 0
PLANETA_POR_DEFECTO = "tierra"

#pedir datos iniciales (altura, tiempo en el que queremos medir, planeta); ATENCIÓN si existe posibilidad de que haya decimales, pon un float
altura_incial = float(input("¿A qué altura empieza el objeto a caer?:"))
tiempo = float(input("¿Cuánto tiempo va a estar cayendo?"))

#Hacemos un if para que la persona pueda escoger un planeta
planeta = input("Disculpe señora delulu, En qué planeta está? (tierra, luna, marte, jupiter, sol) ")

#pasamos a minúsculas el planeta:
planeta = planeta.lower()

#Validamos que la ubicación sea válida:
# osea poner los if-else necesarios para establecer qué ocurre cuando escoges un planeta válido y un planeta inválido.
if planeta in GRAVEDADES:
    #tenemos esta ubicación
    GRAVEDAD = GRAVEDADES [planeta]
else:
    print(f"Chuchi ese planeta no existe ve a la ESO, te pongo la {PLANETA_POR_DEFECTO}.")
    GRAVEDAD = GRAVEDADES[PLANETA_POR_DEFECTO]

#convertimos la funcion a python
altura_actual = altura_incial + ( VELOCIDAD_INICIAL * tiempo) + (0.5 * GRAVEDAD * (tiempo**2))


#Para vacilar pasamos los m a yardas: 
altura_actual *= 1.0936


#Vamos a añadir si a llegado al suelo o no e imprimimos la altura resultado:
if altura_actual <= 0: 
    print(f"El objeto ha crasheado en el suelo tontiiii")
else:
    print( f"La altura en el segundo {tiempo} del objeto es {altura_actual} en yardas. ehhehehe eres un traidor del imperio más grande del mundo el imperio Inglés GOD SAVE THE QUEEN")
