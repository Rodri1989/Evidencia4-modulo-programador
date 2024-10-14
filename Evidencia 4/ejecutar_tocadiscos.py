
from tocadiscos import Tocadiscos

# Crear una instancia del Tocadiscos
tocadiscos = Tocadiscos("Disco A", 33)

# Mostrar el estado inicial del tocadiscos
print(tocadiscos)

# Reproducir una pista
print(tocadiscos.reproducir(2))
print(tocadiscos)  

# Cambiar la velocidad de reproducción
tocadiscos.cambiar_velocidad(45)
print(tocadiscos)  

# Pausar la reproducción
print(tocadiscos.pausar())
print(tocadiscos)  

# Cambiar de disco
tocadiscos.cambiar_disco("Disco B", 78)
print(tocadiscos)  

# Regresar al inicio del disco
print(tocadiscos.regresar_al_inicio())
print(tocadiscos)  
