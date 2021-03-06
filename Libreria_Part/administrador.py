from .particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )


#l01 = Particula(id="2306", origen_x="34", origen_y="47", destino_x="90", destino_y="23", velocidad="80", red="90",  green="2", blue="34", distancia="")
#l02 = Particula(id="2940", origen_x="0", origen_y="0", destino_x="0", destino_y="0", velocidad="0", red="100",  green="200", blue="300", distancia="0")
#Administrador = Administrador()
#Administrador.agregar_final(l01)
#Administrador.agregar_inicio(l02)
#Administrador.agregar_inicio(l01)
#Administrador.mostar()