from clases.Transporte import Transporte
from clases.Vehiculo import Vehiculo
from abc import ABC, abstractmethod 

class Automovil(Transporte,ABC,Vehiculo):
    ruedas = 4

    def __init__(self, color, marca, aceleracion,_ano,__modelo):
        super().__init__(_ano,__modelo)
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = 0
        self.__modelo= __modelo
        self._ano= _ano

    def acelerar(self):
        self.velocidad += self.aceleracion

    def frenar(self):
        self.velocidad -= self.aceleracion


    def conducir(self):
        print("Conduciendo automóvil")

    def volar(self):
        print("volando")
        pass  # No se puede volar en un automóvil
  
    def datos(self):
      if self.ruedas==4:
        return print("automovil:",{"modelo:",self.__modelo},{" ruedas:",self.ruedas})
      else:
        if self.ruedas==6:
           return print("automovil volador:",{"modelo:",self.__modelo},{" ruedas:",self.ruedas})