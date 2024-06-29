from abc import ABC, abstractmethod
class Transporte(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def volar(self):
        pass