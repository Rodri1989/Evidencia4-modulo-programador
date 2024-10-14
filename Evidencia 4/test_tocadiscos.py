import pytest
from tocadiscos import Tocadiscos

def test_estado_inicial():
    tocadiscos = Tocadiscos("Disco A")
    assert tocadiscos.disco == "Disco A"
    assert tocadiscos.velocidad == 33
    assert tocadiscos.pista_actual == 1
    assert tocadiscos.en_reproduccion == False

def test_reproducir_disco():
    tocadiscos = Tocadiscos("Disco A")
    resultado = tocadiscos.reproducir(2)
    assert resultado == "Reproduciendo la pista 2 de Disco A"
    assert tocadiscos.pista_actual == 2
    assert tocadiscos.en_reproduccion == True

def test_reproducir_disco_pista_invalida():
    tocadiscos = Tocadiscos("Disco A")
    with pytest.raises(ValueError):
        tocadiscos.reproducir(0)

def test_pausar_reproduccion():
    tocadiscos = Tocadiscos("Disco A")
    tocadiscos.reproducir()
    resultado = tocadiscos.pausar()
    assert resultado == "Reproducción pausada en la pista 1 de Disco A"
    assert tocadiscos.en_reproduccion == False

def test_pausar_ya_pausado():
    tocadiscos = Tocadiscos("Disco A")
    resultado = tocadiscos.pausar()
    assert resultado == "El tocadiscos ya está pausado"

def test_regresar_al_inicio():
    tocadiscos = Tocadiscos("Disco A")
    tocadiscos.reproducir(3)
    resultado = tocadiscos.regresar_al_inicio()
    assert resultado == "Regresando al inicio de Disco A"
    assert tocadiscos.pista_actual == 1
    assert tocadiscos.en_reproduccion == False

def test_cambiar_velocidad():
    tocadiscos = Tocadiscos("Disco A")
    tocadiscos.cambiar_velocidad(45)
    assert tocadiscos.velocidad == 45

def test_cambiar_velocidad_invalida():
    tocadiscos = Tocadiscos("Disco A")
    with pytest.raises(ValueError):
        tocadiscos.cambiar_velocidad(60)

def test_cambiar_disco():
    tocadiscos = Tocadiscos("Disco A", 33)
    tocadiscos.cambiar_disco("Disco B", 78)
    assert tocadiscos.disco == "Disco B"
    assert tocadiscos.velocidad == 78
    assert tocadiscos.pista_actual == 1
    assert tocadiscos.en_reproduccion == False

def test_str_repr():
    tocadiscos = Tocadiscos("Disco A", 33)
    resultado = str(tocadiscos)
    assert resultado == "Tocadiscos con el disco 'Disco A', velocidad 33 RPM, en la pista 1, estado: pausado"
