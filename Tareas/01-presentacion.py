# strings
nombre = "Luis Andrés"
carrera = "Ingeniería de Informática"

# Integer
edad = 18

# float
estatura = 1.75

# booleans
lenguaje_dominado = True

# list
tecnologias_conocidas = [
    "Python",
    "FASTAPI",
    "JavaScript",
    "HTML",
    "TailwindCSS",
    "SQL",
    "Linux",
    "Docker",
    "Git",
    "GitHub",
    "Django",
    "Django-Rest-Framework ",
]

# tuple
lenguaje_de_programacion_fav = ("Python",)

# set
areas_de_interes: set = {
    "Ciberseguridad",
    "Inteligencia Artificial",
    "Machine Learning",
    "Electrónica",
    "Desarrollo Web",
    "Backend",
}

# Dictionary
proyectos_activos: dict = {
    "FletBeat": "Aplicación backend para descarga de música con FastAPI",
    "AnimalHome": "Plataforma web e-commerce",
    "Laboratorio_Hardware": "Diagnóstico y reparación de placas electrónicas",
}

# ----------------- EJECUCION ---------------------#
print("=" * 65)
print(f"PRESENTACIÓN PERSONAL | {nombre.upper()}")
print("=" * 65)

# Datos Primitivos
print(f"Nombre: {nombre} | Tipo: {type(nombre).__name__}")
print(f"Carrera: {carrera} | Tipo: {type(carrera).__name__}")
print(f"Edad: {edad} años | Tipo: {type(edad).__name__}")
print(f"Estatura: {estatura} m | Tipo: {type(estatura).__name__}")
print(f"Lenguaje dominado: {lenguaje_dominado} | Tipo: {type(lenguaje_dominado).__name__}")
print("-" * 65)

# Lista
print(f"\nTECNOLOGÍAS CONOCIDAS (List | Tipo: {type(tecnologias_conocidas).__name__}):")
for i, tech in enumerate(tecnologias_conocidas, 1):
    print(f"  {i}. {tech.strip()}")

# Tupla
print(f"\nLENGUAJE FAVORITO (Tuple | Tipo: {type(lenguaje_de_programacion_fav).__name__}):")
print(f"  - {lenguaje_de_programacion_fav[0]}")

# Conjunto (Set)
print(f"\nÁREAS DE INTERÉS (Set | Tipo: {type(areas_de_interes).__name__}):")
for area in areas_de_interes:
    print(f"  - {area}")

# Diccionario (Dict)
print(f"\nPROYECTOS ACTIVOS (Dict | Tipo: {type(proyectos_activos).__name__}):")
for proyecto, descripcion in proyectos_activos.items():
    print(f"  - [{proyecto}]: {descripcion}")

print("=" * 65)