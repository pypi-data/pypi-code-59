from win32com.client.connect import *

from CANoe_Python.Application.Bus import Bus
from CANoe_Python.Application.Environment import Environment
from CANoe_Python.Application.Measurement import Measurement
from CANoe_Python.Application.CAPL import CAPL
from CANoe_Python.Application.System import System



class Application:
    def __init__(self):
        self.__application = win32com.client.DispatchEx("CANoe.Application")
        self.__ver = self.__application.Version
        print('Loaded CANoe version ',
              self.__ver.major, '.',
              self.__ver.minor, '.',
              self.__ver.Build, '...')

        self.Bus = Bus(self.__application)
        self.Environment = Environment(self.__application)
        self.Measurement = Measurement(self.__application)
        self.CAPL = CAPL(self.__application)
        self.System = System(self.__application)
