import pandas as pd
import pvlib
from pathlib import Path
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
from weather_data import *
from pynasapower.get_data import query_power
from pynasapower.geometry import point
def predict_power(cords):
    for city in tqdm(cords):
        df=pd.read_csv(os.path.join(output_dir,f"{city}.csv"))
        input_df=pd.DataFrame()
        input_df["Date"] = pd.to_datetime({
            'year':  df['YEAR'],
            'month': df['MO'],
            'day':   df['DY']
        })
        input_df["Date"]=input_df["Date"].dt.tz_localize('Asia/Tehran',nonexistent='shift_forward')
        input_df['ghi_Wm2'] = df['ALLSKY_SFC_SW_DWN'] * 1000.0 /24
        input_df['temp_air']   = df['T2M']
        input_df['wind_speed'] = df['WS10M']
        input_df["T2M"]=df["T2M"]
        input_df.set_index("Date",drop=True,inplace=True)
        input_df = input_df.resample('h').ffill()
 
        dc_power = pvlib.pvsystem.pvwatts_dc(
            effective_irradiance=input_df['ghi_Wm2'],
            temp_cell=input_df["T2M"],
            temp_ref=input_df['temp_air'],
            **module_params
        )
        ac_power = pvlib.inverter.pvwatts(
            pdc=dc_power,
            pdc0=inverter_params['pdc0'],
            eta_inv_nom=inverter_params['eta_inv_nom']
        )
        input_df["P"]=ac_power.values
        df["P (W)"]=input_df.resample('D').sum()["P"].values
        # df['P (W)'] = ac_power *24
        df.to_csv(os.path.join(output_dir,f"{city}.csv"),index=False)
        print(f"{city} : ",df["P (W)"].mean())
# Find the number of weeks for 
def to_week(day):
    if(day<=7):
        return 1
    if(day>7 and day<=14):
        return 2
    if(day>14 and day<=21):
        return 3
    if(day>21 and day<=28):
        return 4
    if(day>28):
        return 5
# Can Be Used To Tell Us The Weekly energy
def calculate_features(df,week,month):
    d=df[(df["week"]==week) & (df["MO"]==month)]
    display(d.head(7))
    display(d.drop(columns=["YEAR","MO"]).groupby("DY").mean())
    year=df["YEAR"].max()
    print(f"predicted features for the year : {year+1} \n month : {month} \n week : {week}")
    display(d.drop(columns=["week","MO","YEAR","DY"]).mean())
    
params=["ALLSKY_SFC_SW_DWN","CLRSKY_SFC_SW_DWN","ALLSKY_SFC_SW_DNI","ALLSKY_SFC_SW_DIFF",
        "ALLSKY_KT","T2M","RH2M","WS10M","CLOUD_AMT_DAY"]
cords={
    'karaj' : point(50.9950, 35.8400, "EPSG:4326"),
    'ardabil' : point(48.2933, 38.2498, "EPSG:4326"),
    'bushehr' : point(50.8203, 28.9234, "EPSG:4326"),
    'shahrekord' : point(50.8650, 32.3150, "EPSG:4326"),
    'tabriz' : point(46.2919, 38.0850, "EPSG:4326"),
    'shiraz' : point(52.5837, 29.5918, "EPSG:4326"),
    'rasht' : point(49.5832, 37.2808, "EPSG:4326"),
    'gorgan' : point(54.4478, 36.8431, "EPSG:4326"),
    'hamadan' : point(48.5150, 34.7981, "EPSG:4326"),
    'bandar_abbas' : point(56.2666, 27.1960, "EPSG:4326"),
    'ilam' : point(46.4226, 33.6369, "EPSG:4326"),
    'isfahan' : point(51.6675, 32.6546, "EPSG:4326"),
    'kerman' : point(57.0788, 30.2830, "EPSG:4326"),
    'kermanshah' : point(47.0650, 34.3142, "EPSG:4326"),
    'ahvaz' : point(48.6706, 31.3183, "EPSG:4326"),
    'yasuj' : point(51.5875, 30.6684, "EPSG:4326"),
    'sanandaj' : point(47.0028, 35.3098, "EPSG:4326"),
    'khorramabad' : point(48.3558, 33.4878, "EPSG:4326"),
    'arak' : point(49.6892, 34.0917, "EPSG:4326"),
    'sari' : point(53.0601, 36.5633, "EPSG:4326"),
    'bojnurd' : point(57.3290, 37.4742, "EPSG:4326"),
    'qazvin' : point(50.0041, 36.2688, "EPSG:4326"),
    'qom' : point(50.8764, 34.6400, "EPSG:4326"),
    'mashhad' : point(59.6168, 36.2605, "EPSG:4326"),
    'semnan' : point(53.3978, 35.5727, "EPSG:4326"),
    'zahedan' : point(60.8629, 29.4963, "EPSG:4326"),
    'birjand' : point(59.2211, 32.8663, "EPSG:4326"),
    'tehran' : point(51.3890, 35.6892, "EPSG:4326"),
    'urmia' : point(45.0728, 37.5524, "EPSG:4326"),
    'yazd' : point(54.3569, 31.8974, "EPSG:4326"),
    'zanjan' : point(48.4787, 36.6736, "EPSG:4326")
}

output_dir="../Dataset/Nasa Datasets/"

# Get 31 City Weather Dataset From Nasa
for city in cords:
    print(city)
    cord=cords[city]
    df=send_req(cord) 
    df.to_csv(os.path.join(output_dir,f"{city}.csv"),index=False)
# Add Week column to each Dataset
for city in cords:
    df=pd.read_csv(os.path.join(output_dir,f"{city}.csv"))
    df["week"]=df["DY"].apply(to_week)
    df.to_csv(os.path.join(output_dir,f"{city}.csv"),index=False)
# Build a system 
selected_pannel="aSiMicro03036" # Choose a model from the module_params_custom_material.csv file
modual_infos=pd.read_csv("./simulation prams/module_params_custom_material.csv",index_col="Model")
module_params = modual_infos.loc[selected_pannel]
pdc0=module_params.loc["Parallel_Strings"]*module_params.loc["Isco"]*module_params.loc["Voco"]
module_params = {
    'gamma_pdc': -0.0038,
    'pdc0':pdc0
}
inverter_params = {
    'pdc0': pdc0,
    'eta_inv_nom': 0.96
}
# Add The power Columns
predict_power(cords)

# Can also see the energy predicted for the next year(2026) by giving the month and the week

week=2
month=3
calculate_features(kerman_df,week,month)


