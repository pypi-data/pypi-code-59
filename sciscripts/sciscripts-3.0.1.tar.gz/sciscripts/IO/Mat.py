# -*- coding: utf-8 -*-
"""
@author: T. Malfatti <malfatti@disroot.org>
@year: 2015
@license: GNU GPLv3 <https://gitlab.com/malfatti/SciScripts/raw/master/LICENSE>
@homepage: https://gitlab.com/Malfatti/SciScripts

Functions for manipulating specific .mat files.
"""

import numpy as np
import os
from glob import glob
from scipy import io#, signal

from sciscripts.Analysis.Analysis import FilterSignal
from sciscripts.Analysis import GPIAS
from sciscripts.IO import Asdf, Hdf5

def GPIASAnalysis(Folders, InfoFiles, AnalysisFolder, GPIASTimeBeforeTTL=100, GPIASTimeAfterTTL=100,
                     FilterFreq=[70, 400], FilterOrder=3, Filter = 'butter', SliceSize=100):

    SliceSizeMS = [SliceSize][0]
    for F, Folder in enumerate(Folders):
        DataInfo = io.loadmat(InfoFiles[F])
        DataInfo['AnimalName'] = Folder.split('_')[-1]

        Rate = np.array(int(DataInfo['Rate'])); TTL = DataInfo['PulseStart']
        Freqs = glob(Folder + '/*.mat')
        GPIASRec = {'Trace': {}, 'Index':{}}

        SliceSize = int(SliceSizeMS * (Rate/1000))

        for Freq in Freqs:
            SFreq = Freq[-9:-4]; SFreq = SFreq.split('_')
            try:
                SFreq = str(int(SFreq[0])*1000) + '-' + str(int(SFreq[1])*1000)
            except ValueError:
                SFreq = str(int(SFreq[0][1:])*1000) + '-' + str(int(SFreq[1])*1000)

            for Key in GPIASRec.keys():
                if SFreq not in GPIASRec[Key].keys(): GPIASRec[Key][SFreq] = {}

            NoOfSamplesBefore = int(round((GPIASTimeBeforeTTL*Rate)*10**-3))
            NoOfSamplesAfter = int(round((GPIASTimeAfterTTL*Rate)*10**-3))
            NoOfSamples = NoOfSamplesBefore + NoOfSamplesAfter

            XValues = (range(-NoOfSamplesBefore, NoOfSamples-NoOfSamplesBefore)
                       /Rate)*10**3

            Start = int(TTL-NoOfSamplesBefore)
            End = int(TTL+NoOfSamplesAfter)

            Data = io.loadmat(Freq)
            Data['Gap'] = Data['Gap'][0,Start:End] * 1000 # in mV
            Data['NoGap'] = Data['NoGap'][0,Start:End] * 1000 # in mV

            Data['Gap'] = FilterSignal(Data['Gap'], Rate,
                                                    FilterFreq,
                                                    FilterOrder, Filter,
                                                    'bandpass')
            Data['NoGap'] = FilterSignal(Data['NoGap'], Rate,
                                                      FilterFreq,
                                                      FilterOrder, Filter,
                                                      'bandpass')

            GPIASRec['Trace'][SFreq]['Gap'] = Data['Gap'][:]
            GPIASRec['Trace'][SFreq]['NoGap'] = Data['NoGap'][:]
            GPIASRec['Index'][SFreq]['Gap'] = Data['Gap'][:]
            GPIASRec['Index'][SFreq]['NoGap'] = Data['NoGap'][:]

            Keys = [['Gap', 'NoGap', 'GPIASIndex']]
            GPIASRec['Index'][SFreq] = GPIAS.IndexCalc(
                                       GPIASRec['Index'][SFreq], Keys,
                                       NoOfSamplesBefore, SliceSize)

            del(Data)

        AnalysisKey = InfoFiles[F].split('/')[1].split('-')
        AnalysisKey[0] = AnalysisKey[0]+'000000'
        AnalysisKey[1] = DataInfo['AnimalName']
        AnalysisKey = '-'.join(AnalysisKey) + '-Sound-Recovery_' + 'GPIAS'
#        Hdf5.DataWrite({'GPIAS': GPIASRec, 'XValues': XValues}, AnalysisKey, AnalysisFile)
        Asdf.Write({'GPIAS': GPIASRec, 'XValues': XValues}, AnalysisFolder + '/' + AnalysisKey+'.asdf')


def DataToMMSS(FileName, StimType=['Sound'], Override={}):
    DirList = glob('KwikFiles/*'); DirList.sort()
    for Stim in StimType:
        if Override != {}:
            if 'Stim' in Override.keys():
                Stim = Override['Stim']

        Exps = Hdf5.ExpPerStimLoad(Stim, DirList, FileName)

        for FInd, RecFolder in enumerate(Exps):
            Path = os.getcwd() + '/' + RecFolder
            ClusterFile = Path + '/SpkClusters.hdf5'
            Clusters = Hdf5.ClustersLoad(ClusterFile)

            Path = os.getcwd() + '/' + RecFolder +'/SepRec/'
            os.makedirs(Path, exist_ok=True)

            for Rec in Clusters.keys():
                RecS = "{0:02d}".format(int(Rec))

                print('Writing files for clustering... ', end='')
                WF = []; ST = []; ChList = []
                for Ch in Clusters[RecS].keys():
                    WF.append(Clusters[RecS][Ch]['Spikes'][:])
                    ST.append(Clusters[RecS][Ch]['Timestamps'][:])
                    ChList.append(Ch)

                data = {'waveforms': np.array(WF, dtype='object'),
                        'spiketimes': np.array(ST, dtype='object'),
                        'ChList': np.string_(ChList)}

                MatName = ''.join(['Exp_', RecS, '.mat'])
                io.savemat(Path+MatName, {'data': data})
                print('Done.')
    return(None)


def KlustaPSTH2Mat(DataFiles, MatFile):
    FiringPattern = {}
    for A, DataFile in enumerate(DataFiles):
        UnitRec = Asdf.Read(DataFile)
        if not UnitRec['PSTH']: continue
        print(DataFile)

        Key = 'File'+str(A)
        FiringPattern[Key] = np.array([], dtype='float32')
        FiringPattern[Key+'_StimType'] = np.array([], dtype=UnitRec['StimType'].dtype)
        for U, Unit in enumerate(UnitRec['PSTH']):
            if not Unit.mean(): continue
            if UnitRec['SpkResp'][U] > 0.05: continue

            FP = Unit.mean(axis=1)

            FiringPattern[Key+'_StimType'] = np.hstack((FiringPattern[Key+'_StimType'],
                                                        UnitRec['StimType'][U]))
            if not len(FiringPattern[Key]): FiringPattern[Key] = np.array([FP]).T
            else: FiringPattern[Key] = np.hstack((FiringPattern[Key],
                                                     np.array([FP]).T))

        if not len(FiringPattern[Key]):
            del(FiringPattern[Key])
            del(FiringPattern[Key+'_StimType'])

    io.savemat(MatFile, FiringPattern)


def GPIASMat2Asdf(Folders, Freqs):
    # Folders = sorted(glob(os.environ['DATAPATH']+'/../DeadFiles/Data/Recovery/2016021?-Recovery-GPIAS'))
    # Freqs = [[8000,10000],[10000,12000],[12000,14000],[14000,16000]]

    for Folder in Folders:
        Animals = sorted([_[:-1] for _ in glob(Folder+'/*/')])
        InfoFiles = sorted(glob(Folder+'/*.mat'))

        for A,Animal in enumerate(Animals):
            Files = glob(Animal+'/*.mat')

            GPIASData = GPIAS.PreallocateDict(Freqs)

            for File in Files:
                Freq = '-'.join([str(int(_)*1000) for _ in File.split('F')[-1].split('.')[0].split('_')])
                Data = io.loadmat(File)

                for Key in ['IndexTrace', 'Trace']:
                    for Tr in ['Gap', 'NoGap']: GPIASData[Key][Freq][Tr].append(Data[Tr][0,:]*1000)

            DataInfo = io.loadmat(InfoFiles[A])
            GPIASData['Rate'] = DataInfo['Rate'][0]
            GPIASData['TTLs'] = DataInfo['PulseStart'][0]

            GPIASData = {'100': GPIASData}

            Asdf.Write(GPIASData, Animal.split('..')[0] + '/'.join(Animal.split('..')[1].split('/')[3:])+'.asdf')
