__author__ = "Lukas Merkle"
__copyright__ = "Copyright 2020, 20.07.20"
__email__ = 'lukas.merkle@tum.de'


import pandas as pd
import numpy as np




class R0State():
    '''
    Class for getting the r0 bol of a given dataset
    '''

    DATA_FILE_EGOLF = "/home/ga36raf/automotiveCloud/Analytics/R0State/data/Means_BOL_ICD1_ICD2.csv"
    TEMPERATURE_EGOLF_DATA = [21,
                              25]  # 23°C +/-2 https://avt.inl.gov/sites/default/files/pdf/battery/usabc_manual_rev2.pdf
    CAPACITY_BOL = 75

    def __init__(self, car_type):

        if car_type == "eGolf":
            self.raw_data = pd.read_csv(DATA_FILE_EGOLF, index_col=0)


        print("* R0State: Read in eGolf")



    def get_r_10s_bol(self, soc, temp):
        '''
        This function interpolates the r0 from the eGolf datasets of https://avt.inl.gov/sites/default/files/pdf/battery/usabc_manual_rev2.pdf
        and returns at the given soc and temp.
        Temp must be in the range 21-25 because this is where the datafrom above was recorded. There is no interpoaltion temperaturewise.
        :param soc: current soc in range [0...1]
        :param temp: current temperature in °C. Has to be in the recording range of 21..25°C
        :return: R0 BOL at the given soc and temp
        '''

        assert temp in TEMPERATURE_EGOLF_DATA
        assert soc <=1 and soc >=0

        capa_now = soc*CAPACITY_BOL
        return np.interp(capa_now, self.raw_data.index, self.raw_data["BOL"])






if __name__ == "__main__":

    r0state = R0State(car_type = "eGolf")
    print(f"R0 bol at soc=50%: {r0state.get_r_10s_bol(0.56, 25)}")

