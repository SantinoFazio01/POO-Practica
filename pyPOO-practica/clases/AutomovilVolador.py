from clases.Automovil import Automovil

class AutomovilVolador(Automovil):
    ruedas = 6
    estaVolando=False

    def __init__(self, color, marca, aceleracion,_ano,__modelo, estaVolando=True):
        super().__init__(color, marca, aceleracion,_ano,__modelo)
        self.estaVolando = estaVolando

    def validarVuelo(self):
      if self==True:
          def vuela(self):
              self.estaVolando = True
              print("esta volando")
      else:
          def noVuela(self):
              self.estaVolando = False
              print("no esta volando")