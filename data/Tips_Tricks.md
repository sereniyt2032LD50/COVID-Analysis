---- This file will contain helpful commands wish I belive will be usefull at very step of the journey

#It is possible to fill missing values in particular columns only. With fillna, and a dictionary for the values 

Examples:
1- df.fillna({'Name': 'XXX', 'Age':'0'})

2- df.fillna(df.mean(numeris_only = True))

3- df.fillna(df.mode().iloc[0])

4- na_fill = pd.Series(['XXX', 20, 100], index = ['Name', 'Age', 'ZZZ'])
   df.fillna(na_fill)

5- df.fillna(method = 'ffill'), df.fillna(method='bfill')


