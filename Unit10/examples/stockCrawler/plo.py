import pandas as pd

pd.read_csv('./2015_tse_2301.csv').plot(labels=['本益比', '殖利率', '股價淨值比'])