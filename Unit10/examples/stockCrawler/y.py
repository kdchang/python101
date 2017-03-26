from yahoo_finance import Share
import datetime
import pandas as pd 
def getStock(id):
	stock = Share(str(id)+'.TW')
	today = datetime.date.today() #todays date
	data = stock.get_historical('2015-01-01', '2015-12-31')
	return data

table = pd.read_csv('./2015_tse_2301.csv')
 
data = getStock(2301)
price = []
for d in data:
	price.append(d['Close'])

price = price[::-1]
#table.ix[:, 3] = price 
#print(table)
print(price[::-1])
se = pd.DataFrame(price, columns=['股價'])
#p = pd.DataFrame([price], columns=[4])
#table['4'] = se.values
#print(se)
table.columns = ['日期', '本益比', '殖利率', '股價淨值比']
result = pd.concat([table, se], axis=1, join_axes=[table.index])
print(result)

with open('./2015_tse_2301_p.csv', 'w') as f:
	f.write(result.to_csv())