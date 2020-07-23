import time
import win32com.client


class Measurement:
    def __init__(self,Application):
        self.__application = Application
        if self.__application != None:
            self.__Measurement = Application.Measurement
        else:
            raise RuntimeError("CANoe is not open,unable to Measurement")

        if(self.__Measurement.Running == True):
            print('Measurement status: Running')
        else:
            print('Measurement status: Not Running')

    def StartMeasurement(self):
        retry = 0
        retry_counter = 5
        while not self.__application.Measurement.Running and (retry < retry_counter):
            self.__application.Measurement.Start()
            time.sleep(1)
            retry += 1
        if (retry == retry_counter):
            raise RuntimeWarning("CANoe start measuremet failed, Please Check Connection!")

    def StopMeasurement(self):
        if self.__application.Measurement.Running:
            self.__application.Measurement.Stop()
        else:
            pass