class Bus:
    def __init__(self,application):
        self.__application = application
        self.__bus = self.__application.GetBus("CAN")

    def GetSignal(self,channel, message, signal):
        if (self.__application != None):
            result = self.__bus.GetSignal(channel, message, signal)
            return result.Value
        else:
            raise RuntimeError("CANoe is not open,unable to GetVariable")

    def SetSignal(self, channel, message, signal, value):
        result = None
        if (self.__application != None):
            result = self.__bus.GetSignal(channel, message, signal)
            result.Value = value
            checker = self.GetSignal(channel, message, signal)
            while (round(checker) != round(value)):
                checker = self.GetSignal(channel, message, signal)
        else:
            raise RuntimeError("CANoe is not open,unable to SetVariable")