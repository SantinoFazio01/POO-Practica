import sqlite3

from clases.Automovil import Automovil
from clases.AutomovilVolador import AutomovilVolador
from clases.Clientes import Clientes
from clases.Conexion import Conexion

auto = Automovil("rojo", "bmw", 70,2022,"3.4")
auto1 = AutomovilVolador("rojo", "bmw", 70,2022,"3.4",True)
obj1 = AutomovilVolador("rojo", "bmw", 70,2022,"3.9")
obj1.ruedas=9


def tipoVe(object):
  return object.datos()

print(tipoVe(auto1))

c1 = Clientes("tatrrrro","fazio",45422650)

con=Conexion("mi_bd/market.db")
con.insert(c1)
con.traerTodo()