import os
import json
import pandas as pd
import numpy as np
def create_df_6classes(metadata,img_path,combine_similar=False):
    if(combine_similar):
        class_mappings={
            "No-Anomaly":0,"Cell":1,
            "Cell-Multi":1,"Hot-Spot":2,
            "Hot-Spot-Multi":2,"Shadowing":3,"Diode":4,
            "Diode-Multi":4,
            "Offline-Module":5}
        class_keys=["No-Anomaly","Cell","Hot-Spot","Shadowing","Diode","Offline-Module"]
    dic={"image_path":[],"class":[]}
    for key in metadata:
        if metadata[key]["anomaly_class"] not in class_keys:
            continue
        dic["image_path"]+=[os.path.join(img_path,metadata[key]["image_filepath"])]
        num_class=class_mappings[metadata[key]["anomaly_class"]]
        dic["class"]+=[num_class]
    df=pd.DataFrame(dic)
    return df , class_mappings , class_keys , len(class_keys)

def create_df_9classes(metadata,img_path,combine_similar=False):
    if(combine_similar):
        class_mappings={
            "No-Anomaly":0,"Cell":1,
            "Cell-Multi":1,"Cracking":2,"Hot-Spot":3,
            "Hot-Spot-Multi":3,"Shadowing":4,"Diode":5,
            "Diode-Multi":5,"Vegetation":6,"Soiling":7,
            "Offline-Module":8}
        class_keys=["No-Anomaly","Cell","Cracking","Hot-Spot","Shadowing","Diode","Vegetation","Soiling","Offline-Module"]
    dic={"image_path":[],"class":[]}
    for key in metadata:
        dic["image_path"]+=[os.path.join(img_path,metadata[key]["image_filepath"])]
        num_class=class_mappings[metadata[key]["anomaly_class"]]
        dic["class"]+=[num_class]
    df=pd.DataFrame(dic)
    return df , class_mappings , class_keys , len(class_keys)
    
img_path="../Dataset/InfraredSolarModules/"
meta_data_path="../Dataset/InfraredSolarModules/module_metadata.json"
with open(meta_data_path, 'r') as f:
    metadata = json.load(f)
df , class_mappings , class_keys , class_count= create_df_6classes(metadata,img_path,combine_similar=True)
print(df)
# df , class_mappings , class_keys , class_count= create_df_9classes(metadata,combine_similar=True)