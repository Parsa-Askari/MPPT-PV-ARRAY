from pynasapower.get_data import query_power
import pandas as pd , datetime
def send_req(points,params):
    df = query_power(
        geometry     = points,
        start        = datetime.date(2024,1,1),
        end          = datetime.date(2025,1,1),
        community    = "re",
        parameters   = params,
        temporal_api = "daily",
        spatial_api  = "point",
        format       = "csv",
        to_file      = False,
    )
    return df