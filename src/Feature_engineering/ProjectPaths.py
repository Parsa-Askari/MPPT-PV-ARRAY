from os.path import join
folder_path='/home/parsa/Masters/Final Project/datasets/MPPT/Data For Validating Models'
output_folder_paths=f"{folder_path}/processed/"
golden_iv_paths=join(output_folder_paths,"golden_iv_curves")
eugene_iv_paths=join(output_folder_paths,"eugene_iv_curves")
cocoa_iv_paths=join(output_folder_paths,"cocoa_iv_curves")

rename_dict = {
    'Time Stamp (local standard time) yyyy-mm-ddThh:mm:ss':     'TimeStamp',
    'POA irradiance CMP22 pyranometer (W/m2)':                  'POA_CMP22',
    'POA irradiance uncertainty (%)':                           'POA_unc',
    'PV module back surface temperature (degC)':                'Mod_Temp',
    'PV module back surface temperature uncertainty (degC)':    'Mod_Temp_unc',
    'Change in CMP22 during I-V scan +/- W/m2':                 'CMP22_delta',
    'Change in Li-COR during I-V scan +/- W/m2':                'LICOR_delta',
    'MT5 cabinet temperature (degC)':                           'Cab_Temp',
    'Dry bulb temperature (degC)':                              'Dry_Temp',
    'Dry bulb temperature uncertainty (degC)':                  'Dry_Temp_unc',
    'Relative humidity (%RH)':                                  'RH',
    'Relative humidity uncertainty (%RH)':                      'RH_unc',
    'Atmospheric pressure (mb)':                                'Pressure',
    'Atmospheric pressure uncertainty (%)':                     'Pressure_unc',
    'Precipitation (mm) accumulated daily total':               'Precip',
    'Direct normal irradiance (W/m2)':                          'DNI',
    'Direct normal irradiance uncertainty (%)':                 'DNI_unc',
    'Direct normal irradiance standard deviation of 1-second samples of 5-second average (W/m2)':  'DNI_std',
    'Global horizontal irradiance (W/m2)':                      'GHI',
    'Global horizontal irradiance uncertainty (%)':             'GHI_unc',
    'Global horizontal irradiance standard deviation of 1-second samples of 5-second average (W/m2)': 'GHI_std',
    'Diffuse horizontal irradiance (W/m2)':                     'DHI',
    'Diffuse horizontal irradiance uncertainty (%)':            'DHI_unc',
    'Diffuse horizontal irradiance standard deviation of 1-second samples of 5-second average (W/m2)': 'DHI_std',
    'Solar QA residual (W/m2) = Direct*cos(zenith) + Diffuse Horiz. Global Horiz': 'QA_residual',
    'PV module soiling derate':                                 'Soiling',
    'Precipitation prior to daily maintenance (mm) accumulated daily total': 'Precip_pre_maint',
    'Number of I-V curve data pairs (n)':                       'Num_IV_pairs',
    'Isc uncertainty (%)':                                      'Isc_unc',
    'Pmp uncertainty (%)':                                      'Pmp_unc',
    'Imp uncertainty (%)':                                      'Imp_unc',
    'Vmp uncertainty (%)':                                      'Vmp_unc',
    'Voc uncertainty (%)':                                      'Voc_unc',
    'FF uncertainty (%)':                                       'FF_unc'
    
}