import pandas as pd
import OpenBlender
import json
import config

def bitcoin_scrape(start="2022-05-22", end="2022-08-12"):
    token = config.data_token
    action = 'API_getObservationsFromDataset'

    parameters = {
        'token': token,
        'id_dataset': '5d4c3b789516290b02fe3e24',
        'date_filter': {'start_date': start,'end_date': end},
    }

    response = OpenBlender.call(action, parameters)

    df = pd.read_json(json.dumps(response['sample']), convert_dates=False, convert_axes=False)
    df['date'] = [OpenBlender.unixToDate(ts, timezone = 'GMT') for ts in df.timestamp]

    df['change'] = df['close'] - df['open']
    df['binary_change'] = [1 if change > 0 else 0 for change in df['change']]

    return df

print(bitcoin_scrape(start="2022-05-22", end="2022-08-12"))