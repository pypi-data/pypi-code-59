#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: T. Malfatti <malfatti@disroot.org>
@date: 20170612
@license: GNU GPLv3 <https://gitlab.com/malfatti/SciScripts/raw/master/LICENSE>
@homepage: https://gitlab.com/Malfatti/SciScripts
"""

import numpy as np
from rpy2 import robjects as RObj
from rpy2.robjects import packages as RPkg


## Level 0
def RCheckPackage(Packages):
    RPacksToInstall = [Pack for Pack in Packages
                       if not RPkg.isinstalled(Pack)]
    if len(RPacksToInstall) > 0:
        print(str(RPacksToInstall), 'not installed. Install now?')
        Ans = input('[y/N]: ')

        if Ans.lower() in ['y', 'yes']:
            from rpy2.robjects.vectors import StrVector as RStrVector

            RUtils = RPkg.importr('utils')
            RUtils.chooseCRANmirror(ind=1)

            RUtils.install_packages(RStrVector(RPacksToInstall))

        else: print('Aborted.')

    else: print('Packages', str(Packages), 'installed.')

    return(None)


def AdjustNaNs(Array):
    NaN = RObj.NA_Real

    for I, A in enumerate(Array):
        if A != A: Array[I] = NaN

    return(Array)


def PToStars(p):
    No = 0
    while p < 0.05 and No < 4:
        p *=10
        No +=1

    return(No)


## Level 1

# Groups = ['Control', 'Tinnitus']
# Labels = ['NaCl', 'Nic', 'Cann', 'Cann+Nic']
# Ax = [
#     np.array(
#         [[ 2.39222586e+01,  4.87871170e+01,  4.73589361e+01, 6.97789282e+01],
#           [ 2.80826092e+01,  5.98093063e+01,  4.87342179e+01, 2.19316244e+01],
#           [ 3.96061122e+01, -1.30746460e+02, -2.33796954e+01, -3.10473585e+02],
#           [-2.76637077e-01,  3.58889043e+01,  1.36149287e+01, -4.63862181e+01],
#           [ 4.05577612e+02, -1.75374746e+00,  1.11700416e+01, 7.60200530e+01],
#           [-6.26932383e+00, -1.21387959e+01,  2.04739511e+01, 1.29642963e+01],
#           [ 1.28607020e+02,  7.13438988e+00,  8.39784086e+01, 1.10543521e+02],
#           [-6.12902641e+00, -3.79562378e+01,  4.09856021e+01, 4.36741352e+01],
#           [-4.63629603e+01,  7.13858485e+01, -2.74427414e+01, 2.90473104e+01],
#           [ 3.51840198e+01, -2.54109311e+02, -1.33715391e+01, -1.09103107e+02],
#           [ 2.68421352e+01,  4.14270699e+01,  7.36609101e+00, 2.41672456e+01]]
#     ),
#     np.array(
#         [[  66.01416767,  -53.88476849,   22.00369239,   30.97251058],
#           [  30.00748754,   47.38330245,  -26.71322823,   39.63605165],
#           [  34.27283764,   13.54150772,   45.98014355,   58.11798275],
#           [   5.95538616,    1.86426044,    7.33567476,   45.65891027],
#           [  20.66245079,   73.09010327,   10.37521362,   45.06258965],
#           [  36.89069152,    1.00836158,   34.75482464,  -15.15245438],
#           [  43.75897646,   58.64500701,  130.06068468,   59.56515372],
#           [  47.2715199 ,   50.70306361,   90.52264988,   68.25714111],
#           [ -10.32551527,  -53.93958092,  -17.11922884, -126.11472607],
#           [  17.21879244,   48.85835648,  178.16992402,  -40.09600878]]
#     )
# ]
# DataFrame = {
#     'Values': np.concatenate([np.ravel(_.T) for _ in Ax]),
#     'Factor1': np.concatenate([[Group]*np.product(Ax[G].shape) for G,Group in enumerate(Groups)]),
#     'Factor2': np.concatenate([np.ravel([[Labels[A]]*G.shape[0] for A in range(G.shape[1])]) for G in Ax]),
#     'Id': np.concatenate([np.ravel([np.arange(0,G.shape[0])]*G.shape[1])+(g*Ax[g-1].shape[0]) for g,G in enumerate(Ax)])
# }
# Data, Factor1, Factor2, Id = DataFrame['Values'], DataFrame['Factor1'], DataFrame['Factor2'], DataFrame['Id']



def RPCA(Matrix):
    RCheckPackage(['stats']); Rstats = RPkg.importr('stats')

    RMatrix = RObj.Matrix(Matrix)
    PCA = Rstats.princomp(RMatrix)
    return(PCA)


def RAnOVa(Data, Factor):
    RCheckPackage(['stats']); Rstats = RPkg.importr('stats')
    RCheckPackage(['base']); Rbase = RPkg.importr('base')

    Weight = RObj.FloatVector(Data)
    Group = RObj.FactorVector(Factor)

    RObj.globalenv["Weight"] = Weight
    RObj.globalenv["Group"] = Group
    Model = Rstats.lm("Weight ~ Group")

    print('='*20)
    print(Rstats.anova(Model))
    print()
    print(Rbase.summary(Model))


def R2WayAnOVa(Data, Factor1, Factor2, Id, RepeatedMeasures=False):
    RCheckPackage(['rstatix']); RPkg.importr('rstatix')

    Weight = RObj.FloatVector(Data)
    Factors = [RObj.FactorVector(_) for _ in [Factor1, Factor2]]
    Idv = RObj.IntVector(Id)

    Frame = RObj.DataFrame({
        'Weight': Weight,
        'Factor1': Factors[0],
        'Factor2': Factors[1],
        'Id': Idv,
    })

    RObj.globalenv["Frame"] = Frame
    RObj.globalenv["Weight"] = Weight
    RObj.globalenv["Factor1"] = Factors[0]
    RObj.globalenv["Factor2"] = Factors[1]
    RObj.globalenv["Id"] = Idv

    if RepeatedMeasures:
        Model = RObj.r('''anova_test(Frame, dv=Weight, wid=Id, within=c(Factor1,Factor2))''')
    else:
        Model = RObj.r('''anova_test(Frame, Weight ~ Factor1*Factor2)''')

    Cols = ['Effect', 'DFn', 'DFd', 'F', 'p', 'p<.05', 'ges']
    Results = {_[0]: np.array(_[1]) for _ in zip(Cols, Model)}
    del(Results['p<.05'])

    return(Results)


def RPwrAnOVa(GroupNo=RObj.NULL, SampleSize=RObj.NULL, Power=RObj.NULL,
           SigLevel=RObj.NULL, EffectSize=RObj.NULL):
    RCheckPackage(['pwr']); Rpwr = RPkg.importr('pwr')

    Results = Rpwr.pwr_anova_test(k=GroupNo, power=Power, sig_level=SigLevel,
                                  f=EffectSize, n=SampleSize)

    print('Running', Results.rx('method')[0][0] + '... ', end='')
    AnOVaResults = {}
    for Key, Value in {'k': 'GroupNo', 'n': 'SampleSize', 'f': 'EffectSize',
                       'power':'Power', 'sig.level': 'SigLevel'}.items():
        AnOVaResults[Value] = Results.rx(Key)[0][0]

    print('Done.')
    return(AnOVaResults)


def RTTest(DataA, DataB, Paired=True, EqualVar=False, Alt='two.sided', Confidence=0.95):
    Rttest = RObj.r['t.test']

    DataA = AdjustNaNs(DataA); DataB = AdjustNaNs(DataB)

    Results = Rttest(RObj.FloatVector(DataA), RObj.FloatVector(DataB),
                     paired=Paired, var_equal=EqualVar, alternative=Alt,
                     conf_level=RObj.FloatVector([Confidence]),
                     na_action=RObj.r['na.omit'])

    TTestResults = {}; Names = list(Results.names)
    for Name in Names:
        TTestResults[Name] = Results.rx(Name)[0][0]

    return(TTestResults)

