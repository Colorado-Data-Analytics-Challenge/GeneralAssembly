from os import listdir
import pandas as pd
from time import strftime, gmtime

df = pd.read_csv('./bird/scoots.csv')
df['date'] = '2018-11-10 20:40:01'

scoot_loc = './Chris/scoot_loc_apipull'
scoot_files = listdir(scoot_loc)
time_dict = {}

for file in scoot_files:
    epoch_time = file[:file.index('_')]
    date_time = strftime('%Y-%m-%d %H:%M:%S', gmtime(float(epoch_time)))

    scoot_file_df = pd.read_csv(f'{scoot_loc}/{file}')
    scoot_file_df['date'] = date_time
    df = pd.concat([df, scoot_file_df], axis=0, sort=False)

df.to_csv('./Shane/combined_scoots.csv')
