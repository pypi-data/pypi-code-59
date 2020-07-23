from CANoe_Python.Application.System.Namespaces import Namespaces

class System:
    def __init__(self,application):
        self.__application = application
        self.__System = self.__application.System
        self.Namespaces = Namespaces(self.__System)
