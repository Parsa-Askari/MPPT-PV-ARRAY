import pandas as pd
import pvlib
from pathlib import Path
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
from weather_data import *
from pynasapower.get_data import query_power
from pynasapower.geometry import point
def predict_power(df):
    input_df=pd.DataFrame()
    input_df["Date"] = pd.to_datetime({
        'year':  df['YEAR'],
        'month': df['MO'],
        'day':   df['DY']
    })
    input_df['ghi_Wm2'] = df['ALLSKY_SFC_SW_DWN'] * 1000.0 / 24.0
    input_df['temp_air']   = df['T2M']
    input_df['wind_speed'] = df['WS10M']
    input_df["T2M"]=df["T2M"]

    module_params = {
        'pdc0':      700, 
        'gamma_pdc': -0.0038,
    }
    inverter_params = {
        'pdc0': 5000,
        'eta_inv_nom': 0.96
    }

    dc_power = pvlib.pvsystem.pvwatts_dc(
        effective_irradiance=input_df['ghi_Wm2'],
        temp_cell=input_df["T2M"],     # uses temp_air & wind_speed internally if you pass them
        temp_ref=input_df['temp_air'],
        **module_params
    )
    ac_power = pvlib.inverter.pvwatts(
        pdc=dc_power,
        pdc0=inverter_params['pdc0'],
        eta_inv_nom=inverter_params['eta_inv_nom']
    )

    input_df['P (W)'] = ac_power

    input_df[["Date","P (W)"]].to_csv(csv_out,index=False)

tbriz = point(44.24,39.26,"EPSG:4326") # get any cord from input
kerman = point(57,30.2,"EPSG:4326")
params=["ALLSKY_SFC_SW_DWN","T2M","QV2M","PS","WS10M",
        "CLRSKY_SFC_SW_DWN","ALLSKY_SFC_SW_DNI","ALLSKY_SFC_SW_DIFF"]

# tbriz_df=send_req(tbriz,params)

kerman_df=send_req(kerman,params)

city="kerman"# change this based on city
csv_in  = Path(f'../Dataset/{city}_w.csv') 
csv_out = Path(f'../Dataset/{city}_power_predictions.csv')

df = pd.read_csv(csv_in)
predict_power(df)