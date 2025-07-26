from .utils import *
def feature_eng(df):
    # remove nan
    df=remove_invalid_rows(df)
    # remove uncorrolated data
    columns=df.columns
    unc_cols = [col for col in df.columns if (col.endswith('_unc') or col.endswith("_std"))]
    lickage_features=["Isc (A)","I-V paths","TimeStamp","FF (%FF)","Voc (V)"]+unc_cols
    corr=(df.drop(columns=lickage_features+["filename"])).corr()
    uncorrlated_cols=[]
    for col in corr.columns : 
        if(corr[col].sum()==0):
            uncorrlated_cols.append(col)
    print("removing these columns : ",uncorrlated_cols)
    df.drop(columns=uncorrlated_cols,inplace=True)
    columns=df.columns

    return df,columns,lickage_features