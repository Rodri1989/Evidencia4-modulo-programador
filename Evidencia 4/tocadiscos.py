class Tocadiscos:
    def __init__(self, disco, velocidad=33):
        self.disco = disco
        self.velocidad = velocidad
        self.pista_actual = 1
        self.en_reproduccion = False

    def reproducir(self, pista=1):
        if pista < 1:
            raise ValueError("El número de pista debe ser mayor o igual a 1")
        self.pista_actual = pista
        self.en_reproduccion = True
        return f"Reproduciendo la pista {pista} de {self.disco}"

    def pausar(self):
        if not self.en_reproduccion:
            return "El tocadiscos ya está pausado"
        self.en_reproduccion = False
        return f"Reproducción pausada en la pista {self.pista_actual} de {self.disco}"

    def regresar_al_inicio(self):
        self.pista_actual = 1
        self.en_reproduccion = False
        return f"Regresando al inicio de {self.disco}"

    def cambiar_velocidad(self, nueva_velocidad):
        if nueva_velocidad not in [33, 45, 78]:
            raise ValueError("Velocidad no válida. Debe ser 33, 45 o 78 RPM")
        self.velocidad = nueva_velocidad

    def cambiar_disco(self, nuevo_disco, velocidad):
        self.disco = nuevo_disco
        self.velocidad = velocidad
        self.pista_actual = 1
        self.en_reproduccion = False

    def __str__(self):
        estado = "reproduciendo" if self.en_reproduccion else "pausado"
        return (f"Tocadiscos con el disco '{self.disco}', "
                f"velocidad {self.velocidad} RPM, en la pista {self.pista_actual}, estado: {estado}")
