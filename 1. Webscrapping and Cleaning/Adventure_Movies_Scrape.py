import selenium
from selenium import webdriver
from time import sleep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#variables
title_list = []
year_list = []
ratings_list = []
total_metascore = []
director_list = []
total_vote_count = []
total_gross = []
genre_list = []
total_duration = []
actor_list1 = []
actor_list2 = []
actor_list3 = []
actor_list4 = []
age_list = []

#pages you want to scrape 
start_page, last_page = 0 , 199
break_page = last_page + 1

page = range(start_page, break_page)

#iterates through the pages (line 34)
for it in page:
    url = "https://www.imdb.com/search/title/?title_type=feature&genres=adventure&sort=num_votes,desc&start=" + str(1+50*it) + "&explore=genres&ref_=adv_nxt"

    #driver relative path
    my_driver = "chromedriver.exe"

    #loading driver with url
    driver = webdriver.Chrome(my_driver)
    driver.get(url)
    sleep(3)

    # m,n are the number of movies displayed on the website (50 movies per page)
    m = 1
    n = 51
    
    #below i will loop through every movie and grabbing the element using xpath and storing into a list as text
    #using try and except so when it tries to find the element and fails it will just put a blank value instead of breaking code.
    #some failed values i will append 0 because it is a quantity feature.

    #title
    for i in range(m,n):
        try:
            title = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/h3/a')
            title_list.append(title.text)
        except Exception:
            title_list.append(np.nan)

    #year
    for i in range(m,n):
        try:
            year = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/h3/span[2]')
            year_list.append(year.text)
        except Exception:
            year_list.append(np.nan)

    #rating
    for i in range(m,n):
        try:
            ratings = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/div/div[1]/strong')
            ratings_list.append(ratings.text)
        except Exception:
            ratings_list.append(np.nan)

    #meta score
    for i in range(m,n):
        try:
            metascore = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) +  ']/div[3]/div/div[3]/span')
            total_metascore.append(metascore.text)
        except Exception:
            total_metascore.append(np.nan)

    #Director
    for i in range(m,n):
        try:
            director = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[3]/a[1]')
            director_list.append(director.text)
        except Exception:
            director_list.append(np.nan)

    #film stars
    for i in range(m,n):
            for j in range(2,6):
                if j == 2:
                    try:
                        actors = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]/a['+str(j)+']')
                        actor_list1.append(actors.text)
                    except Exception:
                        actor_list1.append(np.nan)
                elif j == 3:
                    try:
                        actors = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]/a['+str(j)+']')
                        actor_list2.append(actors.text)
                    except Exception:
                        actor_list2.append(np.nan)
                elif j == 4:
                    try:
                        actors = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]/a['+str(j)+']')
                        actor_list3.append(actors.text)
                    except Exception:
                        actor_list3.append(np.nan)
                else:
                    try:
                        actors = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div['+str(i)+']/div[3]/p[3]/a['+str(j)+']')
                        actor_list4.append(actors.text)
                    except Exception:
                        actor_list4.append(np.nan)

    #gross
    for i in range(m,n):
        try:
            gross = driver.find_element_by_xpath('//html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[4]/span[5]')
            total_gross.append(gross.text)
        except Exception:
            total_gross.append(np.nan)


    #genre
    for i in range(m,n):
        try:
            genre = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[1]/span[5]')
            genre_list.append(genre.text)
        except Exception:
            genre_list.append(np.nan)

    # duration
    for i in range(m,n):
        try:
            Duration = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[1]/span[3]')
            total_duration.append(Duration.text)
        except Exception:
            total_duration.append(np.nan)
            
    #age
    for i in range(m,n):
        try:
            age = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[1]/span[1]')
            age_list.append(age.text)
        except Exception:
            age_list.append(np.nan)

    #Vote count        
    for i in range(m,n):
        try:
            vote_count = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[' + str(i) + ']/div[3]/p[4]/span[2]')
            total_vote_count.append(vote_count.text)
        except Exception:
            total_vote_count.append(np.nan)
    
    sleep(1)
    

#putting all lists into a dictionary
data = {'Title' : title_list, 'Year' : year_list, 'Ratings' : ratings_list,
        'Director' : director_list,'Metascore' : total_metascore,'Vote Count' : total_vote_count ,
         'Gross (Millions)' : total_gross, 'Genre' : genre_list , 'Duration (min)' : total_duration, 'Age' : age_list , 
        'Actor 1' : actor_list1, 'Actor 2' : actor_list2,
        'Actor 3' : actor_list3, 'Actor 4' : actor_list4 
        }


df = pd.DataFrame(data)

print(df)

df.to_csv('Adventure_Movies_' + str(start_page*50) + '_' + str(break_page*50) + '_data.csv', index=False)


#to do
#https://www.imdb.com/search/title/?title_type=feature&genres=adventure&sort=num_votes,desc&start=9951&explore=genres&ref_=adv_nxt
#beyond this page, use click()