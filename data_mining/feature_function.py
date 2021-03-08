import numpy as np
from scipy.fftpack import fft
import scipy as sp
import pandas as pd
from scipy.stats import kurtosis


def fft(row):
    currLunch=[]
    top_five=[]
    fft_freq=[]
    ps=[]
    # val= np.fft.rfft(row)
    # cgm_psd = np.abs(val) ** 2
    N=len(row)
    tempfft=sp.fftpack.fft(row)
    temppsd=np.abs(tempfft)**2
    fftfreq=sp.fftpack.fftfreq(len(temppsd) , 1/30)
   # i=fftfreq>1
    for i in range(0,30):
        if temppsd[i]!=0:
            ps.append(10 * np.log10(temppsd[i]))
    currLunch = ps
    lunch_sorted=sorted(currLunch)
    top_five=lunch_sorted[-5:]
    return top_five

def cgm_vel(row):
    val=[]
    lst=[]
    val=row
    for i in range(1,len(val)):
        lst.append((val[i]-val[i-1])/5)
    lst=max(lst)
    return lst

def max_min(row):
    lst=[]
    lst=np.ptp(row)
    return lst

def rmse(row):
    val=[]
    rms_arr=[]
    row = pd.Series(row)
    row = row.fillna(0)
    row = row.array
    row = np.array_split(row[::-1], 6)
    y = []
    x = []
    i = 1
    for r in row:
        x.append(i)
        r_temp = []
        for k in r:
            if str(k) != 'nan':
                r_temp.append(k)
        r_temp = np.array(r_temp)
        y.append(rms(r_temp))
        i = i + 1
    rms_arr.append(y)
    return rms_arr


def rms(rootm):
    return np.sqrt(np.mean(rootm**2))

def fft_1(row):
    fft_data=[]
    val=row
    row=pd.DataFrame(val)
    N=31
    T=1/N
    f_values = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    fft_values_ = fft(row.values)
    fft_values = 2.0 / N * np.abs(fft_values_[0:N // 2])
    fft_data.append(fft_values.tolist())
    print(fft_data)

def kurtosis_func(row):
    store=[]
    kurt=[]
    for i in row:
        if str(i)!= 'nan':
            store.append(i)
        # = np.array(store)
    kurt.append(kurtosis(store))
    return kurt
