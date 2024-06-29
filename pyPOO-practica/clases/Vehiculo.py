class Vehiculo:

  def __init__(self,_ano,__modelo):
          self.__modelo= __modelo
          self._ano= _ano

  def get_ano(self):
    return self._ano
  def get__modelo(self):
    return self.__modelo
  def set_ano(self,ano):
     self._ano=ano
  def set__modelo(self,modelo):
     self.__modelo=modelo
 