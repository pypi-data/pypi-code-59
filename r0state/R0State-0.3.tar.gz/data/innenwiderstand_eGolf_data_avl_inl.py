'''
This file converts the data from https://avt.inl.gov/search/content/eGolf?page=1 to useable form
Lukas Merkle 2020
'''



import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

def interp(df, new_index):
    """Return a new DataFrame with all columns values interpolated
    to the new_index values."""
    df_out = pd.DataFrame(index=new_index)
    df_out.index.name = df.index.name

    for colname, col in df.iteritems():
        df_out[colname] = np.interp(new_index, df.index, col)

    return df_out


VINs = {"2012": ["2012_BOT.csv", "2012_ICD1.csv", "2012_ICD2.csv"],
     "2140": ["2140_BOT.csv", "2140_ICD1.csv", "2140_ICD2.csv"],
     "5818": ["5818_BOT.csv", "5818_ICD1.csv", "5818_ICD2.csv"],
     "6525": ["6525_BOT.csv", "6525_ICD1.csv", "6525_ICD2.csv"]}


################## READ and interpolate the data #############################
new_index = [0,10,20,30,40,50,60,75]
new_index = list(range(0,75,5))
N = len(new_index)
dfs_vins={}
for vin in VINs.items():

    dfs_vin=[]
    df_vin = pd.DataFrame(index=new_index)
    for file in vin[1]:
        dfs_vin.append(interp(pd.read_csv(file, index_col=0), new_index))
    df_vin["BOL"] = dfs_vin[0]
    df_vin["ICD1"] = dfs_vin[1]
    df_vin["ICD2"] = dfs_vin[2]

    dfs_vins[vin[0]] = df_vin
print(dfs_vins)
###############################################################################


##################### plot the data ###########################################
# Data as is
f, axs = plt.subplots(5,1)
colormap = ["red", "blue", "green", "orange"]
for idx, vin in enumerate(dfs_vins.items()):
    axs[0].plot(vin[1]["BOL"], label="BOL_"+vin[0], color=colormap[idx])
    axs[0].plot(vin[1]["ICD1"], label="ICD1_"+vin[0], linestyle="--", color=colormap[idx])
    axs[0].plot(vin[1]["ICD2"], label="ICD2_"+vin[0], linestyle="-.", color=colormap[idx])

    axs[idx+1].plot(vin[1]["BOL"], label="BOL_" + vin[0], color=colormap[idx])
    axs[idx+1].plot(vin[1]["ICD1"], label="ICD1_" + vin[0], linestyle="--", color=colormap[idx])
    axs[idx+1].plot(vin[1]["ICD2"], label="ICD2_" + vin[0], linestyle="-.", color=colormap[idx])
    axs[idx+1].set_title = vin[0]

axs[0].set_title("all in one")

[a.legend() for a in axs]


# Mean of the Data
df_means_r10 = pd.DataFrame(index = new_index)
mean_bol = np.zeros(N)
mean_icd1 = np.zeros(N)
mean_icd2 = np.zeros(N)
for idx, vin in enumerate(dfs_vins.items()):
    mean_bol += vin[1]["BOL"].values
    mean_icd1 += vin[1]["ICD1"].values
    mean_icd2 += vin[1]["ICD2"].values
mean_bol = mean_bol / 4
mean_icd1 = mean_icd1 / 4
mean_icd2 = mean_icd2 / 4
df_means_r10["BOL"] = mean_bol
df_means_r10["ICD1"] = mean_icd1
df_means_r10["ICD2"] = mean_icd2
df_means_r10.to_csv("Means_BOL_ICD1_ICD2.csv")

f, axs = plt.subplots(1,1)
axs.plot(mean_bol, label="mean bol", color="blue")
axs.plot(mean_icd1, label="mean icd1", color="red")
axs.plot(mean_icd2, label="mean icd2", color="green")
axs.set_title("Means")
axs.legend()
plt.show()
###############################################################################