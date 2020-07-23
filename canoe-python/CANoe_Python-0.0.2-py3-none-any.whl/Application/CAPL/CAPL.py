class CAPL:
    def __init__(self,application):
        self.__application = application
        if self.__application != None:
            self.__CAPL = self.__application.CAPL
        else:
            raise RuntimeError("CANoe is not open,unable to CAPL")

    def GetFunction(self, name):
        if self.__application != None:
            result = self.__CAPL.GetFunction(name)
            return result.Value
        else:
            raise RuntimeError("CANoe is not open,unable to GetFunction")