'''
Usage : import seschtools
-- To read survery data file : # Either filename with full pathname must be supplied or file must be present in the current working directory
data = seschtools.read_file('FILENAME')

-- It returns Dictionary with following key names having data as values .
    FSU : Has FSU Number
    SchFrame : is the Listing schedule
    SchSampleHH : Particulars of Sample households
    Schdl : contains All Schedules' blocks as Dataframe


######## Iteration through each block of all the Schedules 
Schdl=data['Schdl']   # Get Schedule Data 
for schtype in Schdl: # Iterate over Schedule data by schedule type
    print(schtype)
    for schd in Schdl[schtype]: # Iterate over Schedules in each schedule type
        print(schd)
        for blk in Schdl[schtype][schd]: # Iterate over Block of each Schedule
            # Do something
            print(Schdl[schtype][schd][blk])  # Get Block data as pandas dataframe


######## Get Data of Block 12 of Schedule 1 of 18.2
    print( data['Schdl']['18.2']['1']['12'] )
'''

from seschtools.read_file import read_file