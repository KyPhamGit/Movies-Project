import selenium
from selenium import webdriver
from time import sleep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'Film_0_100_data'
csv1 = pd.read_csv(file + '.csv')
df = pd.DataFrame(csv1)

#cleaning using regex
df['Age'] = df['Age'].str.replace('([0-9]+\smin)', '', regex=True)
df['Duration (min)'] = df['Duration (min)'].str.replace('[^0-9]','', regex=True)

#some small cleaning using replace:
df['Duration (min)'] = df['Duration (min)'].str.replace('min', '')
df['Genre'] = df['Genre'].str.replace('Adventure,', " ")
df['Genre'] = df['Genre'].str.replace('Adventure', " ")

df['Year'] = df['Year'].str.replace('(', '')
df['Year'] = df['Year'].str.replace(')', '')
df['Year'] = df['Year'].str.replace('I', '')
df['Gross (Millions)'] = df['Gross (Millions)'].str.replace('$', '')
df['Gross (Millions)'] = df['Gross (Millions)'].str.replace('M', '')

#splitting Genre into sub genres
multi_columns = lambda x: pd.Series([i for i in reversed(x.split(','))])
new_columns = df['Genre'].apply(multi_columns)
new_columns.rename(columns={0:'Sub Genre 1', 1:'Sub Genre 2'},inplace=True)
new_columns = new_columns[['Sub Genre 1','Sub Genre 2']]

# df = df.astype({'Gross (Millions)': np.float64})
# df = df.astype({'Ratings': np.float64})
# df = df.astype({'Votes': np.float64})

print(df)

df.to_csv(file + '_cleaned.csv', index=False)


#to do
#https://www.imdb.com/search/title/?title_type=feature&genres=adventure&sort=num_votes,desc&start=9951&explore=genres&ref_=adv_nxt
#beyond this page, use click()