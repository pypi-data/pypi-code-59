class Environment:
    def __init__(self,application):
        self.__application = application
        if self.__application != None:
            self.__Environment = self.__application.Environment
        else:
            raise RuntimeError("CANoe is not open,unable to Environment")

    def GetVariable (self, var):
        if self.__application != None:
            result = self.__Environment.GetVariable(var)
            return result.Value
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def SetVariable (self, var, value):
        result = None
        if (self.__application != None):
            result = self.__application.Environment.GetVariable(var)
            result.Value = value
            checker = self.GetVariable(var)
            while (round(checker) != round(value)):
                checker = self.GetVariable(var)
        else:
            raise RuntimeError("CANoe is not open,unable to SetVariable")
