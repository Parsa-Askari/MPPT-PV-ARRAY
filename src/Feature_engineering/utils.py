from tqdm.auto import tqdm
import csv
import numpy as np
from os.path import join
import pandas as pd
from sklearn.metrics import  r2_score

def r2_adj(r2,n,p):
    return 1-((1-r2)*((n-1)/(n-p-1)))
def pretty_csv(datasets,iv_path):
    dic={}
    for path in tqdm(datasets):
        with open(path, newline='') as f:
            reader = csv.reader(f)
            print(path)
            next(reader)
            next(reader)
    
            h=next(reader)
            file_name=(path.split("/")[-1]).split('.')[0]
            if (dic == {}):
                headers=h
                header_size=len(headers)
                headers=headers[:38]+headers[40:]
                
                dic={item:[] for item in headers}
                
                dic["I-V paths"]=[]
                dic["filename"]=[]
            
            for name,row in enumerate(reader):
                features,ivs=row[:header_size],row[header_size:]
                features=features[:38]+features[40:]
                
                features[1:]=list(map(float,features[1:]))
                
                features[-1]=int(features[-1])
                N=features[-1]

                currents  = ivs[:N] 
                voltages  = ivs[N:]         
                iv_pairs  = list(zip(currents, voltages))
                iv_pairs=np.array(iv_pairs,dtype=np.float32)
                dic["I-V paths"].append(join(iv_path,f"{file_name}_{name}.npy"))
                np.save(join(iv_path,f"{file_name}_{name}.npy"), iv_pairs)
                for i,header in enumerate(headers):
                    dic[header].append(features[i])
                dic["filename"].append(file_name)

    return pd.DataFrame(dic)

def split_by_site(df,sites):
    dic={}
    for site in sites:
        dic[site]=df[df["filename"]==site]
    return dic
def remove_invalid_rows(df,threshold=50):
    unc_cols = [col for col in df.columns if col.endswith('_unc')]
    mask = (df[unc_cols] < threshold).all(axis=1)
    df = df.loc[mask].reset_index(drop=True)
    return df[(df["DNI_unc"]>=0) & (df["GHI_unc"]>=0) & (df["DHI_unc"]>=0)]

def evaluate(model,x_train,y_train,x_test,y_test):
    y_test_pred=model.predict(x_test)
    y_train_pred=model.predict(x_train)
    if(y_test_pred.ndim == 1):
        y_test_pred=y_test_pred.reshape(-1,1)
        y_train_pred=y_train_pred.reshape(-1,1)
        
    for i,col in enumerate(y_test.columns):
        print(f"R2 For {col} : ")
        r2_test=r2_score(y_pred=y_test_pred[...,i],y_true=y_test[col])
        r2_train=r2_score(y_pred=y_train_pred[...,i],y_true=y_train[col])
        
        r2_adj_te=r2_adj(r2_test,len(x_test),x_test.shape[1])
        r2_adj_tr=r2_adj(r2_train,len(x_train),x_train.shape[1])
        
        print(f"Test R2 : {r2_test} | Train R2 : {r2_train}")
        print(f"Test ADJ-R2 : {r2_adj_te} | Train ADJ-R2 : {r2_adj_tr}")
        if(col=="Vmp (V)"):
            vmp_test_r2=r2_test
            vmp_train_r2=r2_train
            adj_vmp_train_r2=r2_adj_tr
            adj_vmp_test_r2=r2_adj_te
    return (vmp_test_r2,vmp_train_r2,adj_vmp_train_r2,adj_vmp_test_r2)