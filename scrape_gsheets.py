import pandas as pd
import os
import requests
import sys
import io

def getGoogleSheet(spreadsheet_id, gid, outDir, outFile):
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}'
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join(outDir, outFile)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f'CSV file saved to: {filepath}')
        return pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    else:
        print(f'Error downloading Google Sheet: {response.status_code}')
        sys.exit(1)

def get_sheetdata():
    spreadsheet_id = '1mhwOLqPu2F9026EQiVxFPIN1t9RGafGpl-dokaIsm9c'
    
    # Replace these GIDs with the actual GIDs of your sheets
    darko_gid = '142925152' # Assuming 'darko' is the first sheet
    timedecay_gid = '923517192'  # Replace with the actual GID of 'timedecay' sheet
    
    darko = getGoogleSheet(spreadsheet_id, darko_gid, '', 'darko.csv')
    time_decay = getGoogleSheet(spreadsheet_id, timedecay_gid, '', 'timedecay.csv')
    if 'date' in time_decay.columns:
        time_decay.drop(columns='date',inplace=True)
    
    return darko, time_decay

darko,time_decay=get_sheetdata()
print('Printing first row of DARKO table')

print(darko.iloc[0])

print('Printing first row of Time Decay table')
print(time_decay.iloc[0])
