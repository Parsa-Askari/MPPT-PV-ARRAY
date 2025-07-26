from joblib import load
import pandas as pd
import numpy as np
from Feature_engineering.FE import *
from Feature_engineering.utils import *
from Feature_engineering.ProjectPaths import *

chosen_models=["mSi0247","CIGS1-001","mSi460BB"] # solar models that can be selected in the app

ip_features=["GHI","DNI","POA_CMP22","Mod_Temp"]
ip_labels=["Imp (A)","Pmp (W)"]
v_features=["Cab_Temp","Dry_Temp","Mod_Temp","Pressure","RH","QA_residual","GHI","DNI"]

def predict_and_evaluate(reg_model,v_model,df):
    ip_preds=reg_model.predict(df[ip_features])
    ip_preds=pd.DataFrame(np.concatenate((ip_preds,df[v_features].to_numpy()),axis=1),
                              columns=v_features+["i","p"])
    

    evaluate(v_model,ip_preds,df[["Vmp (V)"]],ip_preds,df[["Vmp (V)"]])

def main():
    for pannel_model in chosen_models:
        df=pd.read_csv(f"../Dataset/{pannel_model}.csv")
        reg_model=load(f"../Best Models/{pannel_model}_hist_i_reg_model.joblib")
        v_hist_model=load(f"../Best Models/{pannel_model}_hist_v_model.joblib")
        predict_and_evaluate(reg_model,v_hist_model,df)

if __name__ == "__main__":
    main()