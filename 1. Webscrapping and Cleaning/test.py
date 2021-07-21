import selenium
from selenium import webdriver
from time import sleep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import selenium
# from selenium import webdriver
# from time import sleep
# import pandas as pd
# import matplotlib as plt
# import seaborn as sns

#variables
title_list = []
year_list = []
ratings_list = []
total_metascore = []
director_list = []
total_votes = []
total_gross = []
genre_list = []
total_duration = []
actor_list1 = []
actor_list2 = []
actor_list3 = []
actor_list4 = []
age_list = []

#range look for the webpages range(0,1) is the first page 
page = range(0,11)

url = "https://www.imdb.com/search/title/?title_type=feature&genres=adventure&sort=num_votes,desc&start=" + str(1+450) + "&explore=genres&ref_=adv_nxt"

#driver relative path
my_driver = "chromedriver.exe"

#loading driver with url
driver = webdriver.Chrome(my_driver)
driver.get(url)
sleep(3)


n = 51

for i in range(1,n):
    try:
        title = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/h3/a')
        title_list.append(title.text)
    except Exception:
        title_list.append("Na")

#year
for i in range(1,n):
    try:
        year = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/h3/span[2]')
        year_list.append(year.text)
    except Exception:
        year_list.append("Na")

#rating
for i in range(1,n):
    try:
        ratings = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/div/div[1]/strong')
        ratings_list.append(ratings.text)
    except Exception:
        ratings_list.append("Na")

#meta score
for i in range(1,n):
    try:
        metascore = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) +  ']/div[3]/div/div[3]/span')
        total_metascore.append(metascore.text)
    except Exception:
        total_metascore.append("Na")

#Director

for i in range(1,n):
    try:
        director = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[3]/a[1]')
        director_list.append(director.text)
    except Exception:
        director_list.append("Na")

#film stars
for i in range(1,n):
    for j in range(2,6):
        films = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]/a['+str(j)+']')
        if j == 2:
            actor_list1.append(films.text)
        elif j == 3:
            actor_list2.append(films.text)
        elif j == 4:
            actor_list3.append(films.text)
        else:
            actor_list4.append(films.text)

#votes
for i in range(1,n):
    try:
        stars = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/div/div[1]/strong')
        total_votes.append(stars.text)
    except Exception:
        total_votes.append("Na")

#gross
for i in range(1,n):
    try:
        gross = driver.find_element_by_xpath('//html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[4]/span[5]')
        total_gross.append(gross.text)
    except Exception:
        total_gross.append("Na")


#genre
genre = driver.find_elements_by_xpath('//span[@class="genre"]')
for row in genre:
    genre_list.append(row.text)

# duration
for i in range(1,n):
    try:
        Duration = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[1]/span[3]')
        total_duration.append(Duration.text)
    except Exception:
        total_duration.append("Na")
        
#age
for i in range(1,n):
    try:
        age = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[1]/span[1]')
        age_list.append(age.text)
    except Exception:
        age_list.append("Na")
            

clean_total_metascore = []
clean_total_duration = []

data = {'Title' : title_list, 'Year' : year_list, 'Ratings' : ratings_list,
        'Director' : director_list,'Metascore' : total_metascore,'Votes' : total_votes , 'Gross (Millions)' : total_gross,
        'Genre' : genre_list , 'Duration (min)' : total_duration, 'Age' : age_list , 
        'Actor 1' : actor_list1, 'Actor 2' : actor_list2,
        'Actor 3' : actor_list3, 'Actor 4' : actor_list4 
        }


for i in page:
    number_elements = 1 + ((i + 1)*50)

df = pd.DataFrame(data)

df['Title'] = df['Title'].str.replace('Na', '')
df['Year'] = df['Year'].str.replace('Na', '')
df['Ratings'] = df['Ratings'].str.replace('Na', '')
df['Director'] = df['Director'].str.replace('Na', '')
df['Metascore'] = df['Metascore'].str.replace('Na', '')
df['Votes'] = df['Votes'].str.replace('Na', '')
df['Gross (Millions)'] = df['Gross (Millions)'].str.replace('Na', '0')
df['Genre'] = df['Genre'].str.replace('Na', '')
df['Duration (min)'] = df['Duration (min)'].str.replace('Na', '')
df['Duration (min)'] = df['Duration (min)'].str.replace('[^0-9]','0', regex=True)
df['Age'] = df['Age'].str.replace('Na', '')


df['Metascore'] = df['Metascore'].str.replace('Metascore', '')
df['Duration (min)'] = df['Duration (min)'].str.replace('min', '')


df['Year'] = df['Year'].str.replace('(', '')
df['Year'] = df['Year'].str.replace(')', '')
df['Year'] = df['Year'].str.replace('I', '')
df['Gross (Millions)'] = df['Gross (Millions)'].str.replace('$', '')
df['Gross (Millions)'] = df['Gross (Millions)'].str.replace('M', '')


# df = df.astype({'Gross (Millions)': np.float64})
df = df.astype({'Ratings': np.float64})
df = df.astype({'Votes': np.float64})

print(df)

df.to_csv(r'test.csv', index=False)


#your data shifts when pathx is absent, set criteria for AGE,Duration