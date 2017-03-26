import pandas as pd

res = pd.read_csv('./lvr_landcsv_201703/A_LVR_LAND_A.csv', encoding='big5')

print(res.describe())
print(res.mean())

with open('./statistic.csv', 'w') as f:
	f.write(res.describe().to_csv())
