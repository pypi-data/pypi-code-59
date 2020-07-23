from CANoe_Python.Application.System.Namespaces.Namespace import Namespace

class Namespaces:
    def __init__(self,system):
        self.__system = system
        self.__Namespaces = self.__system.Namespaces
        self.Namespace = Namespace(self.__Namespaces)
