import os

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
from sklearn.metrics import mean_squared_error
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


if __name__ == "__main__":
    print("Evaluating training data ...")
    parser = argparse.ArgumentParser()
    parser.add_argument("test", metavar="test", type=str, nargs='?')
    args = parser.parse_args()
    test_file_path = args.test

    cgm_nm = [pd.read_csv(csv_data_dir + 'mealAmountData{}.csv'.format(i), header=None, skiprows=1 , names=["Score"]) for i in range(1, 6)]
    frames = [cgm_nm[0].head(n=50), cgm_nm[1].head(n=50), cgm_nm[2].head(n=50) , cgm_nm[3].head(n=50), cgm_nm[4].head(n=50)]
    cgm_nm = pd.concat(frames, sort=False)
    cgm_nm = pd.DataFrame(cgm_nm)
    cgm_nm = cgm_nm.iloc[: :1]
    cgm_nm.column = ["Score"]
    cgm_nm.reset_index(drop=True, inplace=True)
    #print(cgm_nm)

    cgm_m = read_meal_data()

    concat_frame = pd.concat([cgm_m, cgm_nm], axis=1, sort=False)
    #concat_frame = pd.append(cgm_m, cgm_nm, left_index=False, right_index=False, how='left')
    concat_frame.dropna(thresh=15, inplace=True)
    concat_frame.reset_index(drop=True, inplace=True)
    final_m_cgm = clean_data(concat_frame)
    #print(final_m_cgm)
    #
    bins = [-1,0, 20, 40, 60, 80, 100]
    labels =[1,2,3,4,5,6]
    concat_frame["binned"] = pd.cut(final_m_cgm['Score'], bins)
    concat_frame["binned"] = pd.cut(final_m_cgm['Score'], bins, labels=labels)
    #print(concat_frame)
    label_shuffled = concat_frame.iloc[: , 30: ]
    label_shuffled=label_shuffled.iloc[:  ,-1 ]

    label_shuffled = pd.DataFrame(label_shuffled)

    label_shuffled.columns = ['label']
    bin1 = (set(label_shuffled.loc[label_shuffled['label'] == 1].index))
    bin2 = (set(label_shuffled.loc[label_shuffled['label'] == 2].index))
    bin3 = (set(label_shuffled.loc[label_shuffled['label'] == 3].index))
    bin4 = (set(label_shuffled.loc[label_shuffled['label'] == 4].index))
    bin5 = (set(label_shuffled.loc[label_shuffled['label'] == 5].index))
    bin6 = (set(label_shuffled.loc[label_shuffled['label'] == 6].index))
    concat_matrix_san_label = concat_frame.iloc[:, : -2]

    feature_meal = feautre_extract(concat_matrix_san_label)
    normalized_feature_matrix, norms = normalize(feature_meal, axis=0, return_norm=True)
    n = 5
    pca = PCA(n_components=n)
    comp = pca.fit(normalized_feature_matrix)
    normalized_feature_matrix = pca.transform(normalized_feature_matrix)

    km = KMeans(n_clusters=6, max_iter=600, tol=1e-6)
    km.fit(normalized_feature_matrix)
    pickle.dump(km, open("km.pkl", "wb"))
    kmeans_labels_train = km.labels_
    df = pd.DataFrame(kmeans_labels_train)
    df.columns = ['label']
    clust_main = []
    clust0 = (set(df.loc[df['label'] == 0].index))
    clust1 = (set(df.loc[df['label'] == 1].index))
    clust2 = (set(df.loc[df['label'] == 2].index))
    clust3 = (set(df.loc[df['label'] == 3].index))
    clust4 = (set(df.loc[df['label'] == 4].index))
    clust5 = (set(df.loc[df['label'] == 5].index))


    def get_bin_km(clusts, bins):
        lst = []
        for clust in clusts:
            lst = {}
            for bin_key in bins:
                a = set(clust).intersection(set(bins[bin_key]))
                lst[bin_key] = (len(a))
            stats = lst
            del_key = (max(stats.items(), key=operator.itemgetter(1))[0])
            del bins[del_key]
            # x = lst.index(max(lst)) + 1
            clust_main.append(del_key)
        return clust_main


    bins = {}
    bins['b1'] = bin1
    bins['b2'] = bin2
    bins['b3'] = bin3
    bins['b4'] = bin4
    bins['b5'] = bin5
    bins['b6'] = bin6

    clusts = []
    clusts.append(clust0)
    clusts.append(clust1)
    clusts.append(clust2)
    clusts.append(clust3)
    clusts.append(clust4)
    clusts.append(clust5)

    bin_clust0 = get_bin_km(clusts, bins)
    df['label'] = df.replace(0, bin_clust0[0])
    df['label'] = df.replace(1, bin_clust0[1])
    df['label'] = df.replace(2, bin_clust0[2])
    df['label'] = df.replace(3, bin_clust0[3])
    df['label'] = df.replace(4, bin_clust0[4])
    df['label'] = df.replace(5, bin_clust0[5])

    df['label'] = df.replace("b4", 4)
    df['label'] = df.replace('b1', 1)
    df['label'] = df.replace('b2', 2)
    df['label'] = df.replace('b3', 3)
    df['label'] = df.replace('b5', 5)
    df['label'] = df.replace('b6', 6)
    #print(clust_main)
    #print(df)
    normalized_feature_matrix= (pd.DataFrame(normalized_feature_matrix))
    km_result = pd.concat([normalized_feature_matrix, df ], axis=1)
    #print(km_result)
    km_result.to_csv("./results/km_results.csv" , index = False)

    calc = df.where(df.values == label_shuffled.values).notna()
    fls = len(calc) - calc.sum()
    sse = mean_squared_error(df.values, label_shuffled.values)
    print("K means sse", sse)
    acc = (((238 - fls) / 238) * 100)
    #print("K means Accuracy ", acc.iloc[-1])
    max_label = df.label.mode()[0];
    #(max_label)

    #db= DBSCAN(eps=0.072, min_samples=5)
    #db = DBSCAN(eps=0.06, min_samples=4)
    db = DBSCAN(eps=0.07, min_samples=5)
    db.fit(normalized_feature_matrix)
    pickle.dump(db, open("db.pkl", "wb"))
    dbscan_label_train=db.labels_
    df= pd.DataFrame(dbscan_label_train)
    df.columns = [ 'label']
    clust_main=[]
    clust0 = (set(df.loc[df['label'] == 0].index))
    clust1 = (set(df.loc[df['label'] == 1].index))
    clust2 = (set(df.loc[df['label'] == 2].index))
    clust3 = (set(df.loc[df['label'] == 3].index))
    clust4 = (set(df.loc[df['label'] == 4].index))
    clust5 = (set(df.loc[df['label'] == 5].index))


    def get_bin( clusts , bins):
        lst =[]
        for clust in clusts:
            lst = {}
            for bin_key in bins:
              a= set(clust).intersection(set(bins[bin_key]))
              lst[bin_key]=(len(a))
            stats = lst
            del_key= (max(stats.items(), key=operator.itemgetter(1))[0])
            del bins[del_key]
            #x = lst.index(max(lst)) + 1
            clust_main.append(del_key)
        return clust_main

    bins = {}
    bins['b1'] = bin1
    bins['b2'] = bin2
    bins['b3'] = bin3
    bins['b4'] = bin4
    bins['b5'] = bin5
    bins['b6'] = bin6

    clusts =[]
    clusts.append(clust0)
    clusts.append(clust1)
    clusts.append(clust2)
    clusts.append(clust3)
    clusts.append(clust4)
    clusts.append(clust5)

    bin_clust0 = get_bin(clusts, bins)
    df['label']= df.replace(0,bin_clust0[0])
    df['label'] = df.replace(1, bin_clust0[1])
    df['label']= df.replace(2, bin_clust0[2])
    df['label']= df.replace(3, bin_clust0[3])
    df['label']= df.replace(4, bin_clust0[4])
    df['label']= df.replace(5, bin_clust0[5])

    df['label'] = df.replace( "b4", 4)
    df['label'] = df.replace( 'b1', 1)
    df['label'] = df.replace( 'b2', 2)
    df['label'] = df.replace( 'b3' , 3)
    df['label'] = df.replace('b5', 5)
    df['label'] = df.replace('b6',6)
    #(clust_main)
    #print(df)
    db_result = pd.concat([normalized_feature_matrix, df], axis=1)
    db_result.drop(db_result.index[1])
    db_result.to_csv('./results/db_results.csv' , index = False)
    calc = df.where(df.values == label_shuffled.values).notna()
    fls = len(calc)-calc.sum()
    sse = mean_squared_error(df.values, label_shuffled.values)
    print("DBSCAN sse" , sse)
    acc = (((238-fls)/238)*100)
    #print("DBSCAN Accuracy ", acc.iloc[-1])

    #print(clust_main.index(0))
    max_label = df.label.mode()[0];
    # (max_label)
    lbl1 = db.labels_
    #print((lbl1))
    lbl2 = np.where(lbl1==max_label)

    df2=final_m_cgm.copy()
    df2["labels"] = dbscan_label_train
    df2.to_csv("./results/dbscan_train_results.csv")

