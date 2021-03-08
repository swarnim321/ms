import os
import sys
import coordinates as coordinates
import pandas as pd
import numpy as np
import math
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, KFold
from sklearn import svm
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import statistics as statistics
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
import operator
from sklearn.externals import joblib
import pickle

from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import argparse
from feature_function import *

# feature extraction
def feautre_extract(final_cgm):
    val = final_cgm.values
    fft_list = []
    cgm_vel_list = []
    max_min_list = []
    rms_list = []
    rms_list_temp = []
    kurt_list=[]

    for row in val:
        #fft_list.append(fft(row))
        cgm_vel_list.append(cgm_vel(row))
        max_min_list.append(max_min(row))
        rms_list_temp.append(rmse(row))
        kurt_list.append(kurtosis_func(row))
    for i in range(len(rms_list_temp)):
        rms_list.append(rms_list_temp[i][0])

    fft_df = pd.DataFrame(fft_list)
    # variance_df=pd.DataFrame(variance_list)
    max_min_df = pd.DataFrame(max_min_list)
    cgm_vel_df = pd.DataFrame(cgm_vel_list)
    rms_df = pd.DataFrame(rms_list)
    kurt_df= pd.DataFrame(kurt_list)
    feature_matrix = pd.concat([fft_df, cgm_vel_df, max_min_df, rms_df, kurt_df], axis=1)
    feature_matrix = feature_matrix.T.reset_index(drop=True).T
    feature_matrix.shape
    feature_matrix.fillna(0, inplace=True)
    feature_mat = StandardScaler().fit_transform(feature_matrix)
    return feature_mat

def get_col_nan(row_df_na, end=False):
    col_nan = []
    if end:
        row_df_na = row_df_na.iloc[::-1]
    for key, val in row_df_na.iteritems():
        if math.isnan(val):
            col_nan.append(key)
        else:
            break
    return col_nan


def set_col_val(row_df_na, col_nan):
       for col in col_nan:
           row_df_na.iloc[col] = np.nan

# interpolate
def interpolate(cgm_df):
    index_row_na = []
    nan_count_row = cgm_df.isnull().sum(axis=1)
    for key, value in nan_count_row.iteritems():
        if value > 0:
            index_row_na.append(key)
    for index in index_row_na:
        df_na = cgm_df.iloc[index]
        #print(df_na)
        if math.isnan(df_na.iloc[0]) or math.isnan(df_na.iloc[-1]):
            start_nan_val = get_col_nan(df_na)
            last_nan_val = get_col_nan(df_na, True)
            df_na = df_na.interpolate(method='linear')
            set_col_val(df_na, start_nan_val)
            set_col_val(df_na, last_nan_val)
            cgm_df.iloc[index] = df_na
        else:
            df_na = df_na.interpolate(method='linear', limit_direction='forward')
            cgm_df.iloc[index] = df_na
        #print(cgm_df)
    return cgm_df

def clean_data(cgm_m):
        final_m_cgm=interpolate(cgm_m)
        final_m_cgm = final_m_cgm.interpolate(method='linear')
        return final_m_cgm

#if __name__ == "__main__":
curr_dir = os.getcwd()
csv_data_dir = curr_dir + os.sep  + 'Data' + os.sep

    # reading and cleaning Meal  data
def read_meal_data ():
        #cgm_m = [pd.read_csv(csv_data_dir + 'mealData{}.csv'.format(i), header = 0, engine ='python' , sep =',',usecols=list(range(0,30)) ) for i in range(1, 6)]
        frames=[]
        for i in range(1, 6):
         cgm_m =pd.read_csv(csv_data_dir + 'mealData{}.csv'.format(i), names=list(range(29, -1, -1)) )
        #frames = [cgm_m[0].head(n=50), cgm_m[1].head(n=50), cgm_m[2].head(n=50), cgm_m[3].head(n=50), cgm_m[4].head(n=50)]
         frames.append(cgm_m.head(n=50))
        cgm_m = pd.concat(frames, sort=False)
        #df = pd.read_csv(csv_data_dir + 'mealData5.csv', index_col=None, header=None, engine ='python' , sep ='/')
        #cgm_m = cgm_m.iloc[:, 0:31]
        #print (df)
        cgm_m = cgm_m[cgm_m.columns[::-1]]
        #cgm_m.dropna(thresh=15, inplace=True)
        cgm_m.reset_index(drop=True, inplace=True)
        return cgm_m

    # reading and cleaning No Meal  data
def read_no_meal_data():
        cgm_nm = [pd.read_csv(csv_data_dir + 'Nomeal{}.csv'.format(i), header=None, skiprows=1) for i in range(1, 6)]
        frames = [cgm_nm[0], cgm_nm[1], cgm_nm[2], cgm_nm[3], cgm_nm[4]]
        cgm_nm = pd.concat(frames, sort=False)
        cgm_nm = cgm_nm.iloc[:, 0:31]
        cgm_nm = cgm_nm[cgm_nm.columns[::-1]]
        #cgm_nm.dropna(thresh=15, inplace=True)
        cgm_nm.reset_index(drop=True, inplace=True)
        return cgm_nm


    #final_nm_cgm=interpolate(cgm_nm)
    #final_nm_cgm = final_nm_cgm.interpolate(method='linear')


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        #distance+=np.sqrt(np.sum((instance1[x] - instance2[x]) ** 2))
        distance += pow((instance1[x] - instance2[x]), 2)
    #return distance
    return math.sqrt(distance)

def euclideanDistance2(instance1, instance2, length):
    distance2 = 0
    for x in range(length):
        distance2 += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance2)

def getNeighbours(training , testing , k):
    distances = []
    length2 = len(testing) -1
    training = training.values.tolist()
    for y in range (len(training)):
        dist = euclideanDistance2(testing, training[y], length2)
        distances.append((training[y], dist))
        #distances.append(dist)
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for y in range(k):
        neighbors.append(distances[y][0])
        #print(distances[y][0])

    return neighbors


# def getKNeighbors(trainingSet, testInstance, k):
#     distances = []
#     length2 = len(testInstance)
#     for y in range(len(trainingSet)):
#         dist = euclideanDistance2(testInstance, trainingSet[y], length2)
#         distances.append((trainingSet[y], dist))
#     distances.sort(key=operator.itemgetter(1))
#     neighbors = []
#     for y in range(k):
#         neighbors.append(distances[y][0])
#     return neighbors

def getResponse(neighbors):
    cv = {}
    for x in range(len(neighbors)):

        response = neighbors[x][-1]
        #print(neighbors)
        if response in cv:
            cv[response] += 1
        else:
            cv[response] = 1
    sortedVotes = sorted(cv.items(), key=operator.itemgetter(1), reverse=True)
    #print(sortedVotes)
    return sortedVotes[0][0]

def main_func(filepath):
    concat_frame = pd.read_csv(filepath, header=None, usecols=range(0, 30), index_col = False)
    print("Evaluating testing data ...")
    final_m_cgm = clean_data(concat_frame)
    km_results = pd.read_csv('./results/km_results.csv')
    db_results = pd.read_csv('./results/db_results.csv')

    feature_meal = feautre_extract(final_m_cgm)
    normalized_feature_matrix, norms = normalize(feature_meal, axis=0, return_norm=True)
    n = 5
    pca = PCA(n_components=n)
    comp = pca.fit(normalized_feature_matrix)
    normalized_feature_matrix = pca.transform(normalized_feature_matrix)
    res =[]
    res_final=[]

    for row_nrml in normalized_feature_matrix:
            res_inner = []
        #for index, row_km in km_results.iterrows():
            neighbors = getNeighbours(km_results, list(row_nrml), 1)
            res_inner.append( getResponse(neighbors))
            res.append(max(set(res_inner), key =res_inner.count))


    for item in res:
        res_final.append(int(item))
    #print(type(res_final[0]))
    res_final = pd.DataFrame(res_final)
    #print(res_final)

    res = []
    res_final2 = []

    for row_nrml in normalized_feature_matrix:
        res_inner = []
        # for index, row_km in km_results.iterrows():
        neighbors = getNeighbours(db_results, list(row_nrml), 25)
        res_inner.append(getResponse(neighbors))
        res.append(max(set(res_inner), key=res_inner.count))

    for item in res:
        res_final2.append(int(item +2))
    #print(type(res_final2[0]))
    res_final2 = pd.DataFrame(res_final2)

    con = pd.concat([res_final,res_final2], axis = 1)
    #print(res_final2)
    np.savetxt("./proj3_test_results.csv", con, delimiter=",", fmt='%i')

arg= (sys.argv)
param = str(arg[1])
main_func(param)
