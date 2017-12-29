import pandas as pd
from pandas import Series,DataFrame

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ar_df = pd.read_csv('csv/air_reserve.csv')
asi_df = pd.read_csv('csv/air_store_info.csv')
avd_df = pd.read_csv('csv/air_visit_data.csv')
hr_df = pd.read_csv('csv/hpg_reserve.csv')
hsi_df = pd.read_csv('csv/hpg_store_info.csv')
sir_df = pd.read_csv('csv/store_id_relation.csv')
sample_df = pd.read_csv('csv/sample_submission.csv')

# longitude-latitude cluster
xh = hsi_df['longitude']
yh = hsi_df['latitude']
plt.scatter(xh,yh)
plt.show()

xa = asi_df['longitude']
ya = asi_df['latitude']
plt.scatter(xa,ya)
plt.show()

# location counting
asi_location_df = pd.DataFrame(asi_df.air_area_name.str.split(' ', 2).tolist(), columns = ['province','city', 'street'])
asi_df = asi_df.join(asi_location_df)
asi_df.drop(['air_area_name'], axis=1, inplace=True)
asi_province = asi_df['province'].value_counts()
asi_city = asi_df['city'].value_counts()
asi_street = asi_df['street'].value_counts()

hpg_location_df = pd.DataFrame(hsi_df.hpg_area_name.str.split(' ', 2).tolist(), columns = ['province','city', 'street'])
hsi_df = hsi_df.join(hpg_location_df)
hsi_df.drop(['hpg_area_name'], axis=1, inplace=True)
hpg_province = hsi_df['province'].value_counts()
hpg_city = hsi_df['city'].value_counts()
hpg_street = hsi_df['street'].value_counts()

province_count = pd.concat([asi_province, hpg_province]).size # 22
city_count = pd.concat([asi_city, hpg_city]).size # 127
street_count = pd.concat([asi_street, hpg_street]).size # 201
loaction_total = province_count + city_count + street_count # 350
print('loaction_total:', loaction_total)
