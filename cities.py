import pandas as pd


df=pd.read_csv('Resources/cities.csv')
cities_html = df.to_html(classes=None, border=None, justify=None, index=False)
print(cities_html)

