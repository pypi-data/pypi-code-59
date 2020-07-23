class Namespace:
    def __init__(self,namespaces):
        self.__namespaces = namespaces

    def GetSysVar(self, Namespace, Name):
        if (self.__namespaces != None):
            return self.__namespaces(Namespace).Variables(Name).Value
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def SetSysVar(self, Namespace, Name, value):
        if (self.__namespaces != None):
            self.__namespaces(Namespace).Variables(Name).Value = value
            checker = self.GetSysVar(Namespace, Name)
            while (round(checker) != round(value)):
                checker = self.GetSysVar(Namespace, Name)
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")
