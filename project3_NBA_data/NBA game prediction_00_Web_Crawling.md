# NBA game prediction_01_Web_Crawling

semi project part3.

> This project is just part of my practice, so something went wrong and looks like amateur, it's alright! I am sure I am getting better and better and that is my goal :)

* We were looking for something fun to use data and some models for ML/DL.

- Got the data from kaggle (https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018)
- Actually we were trying to use web crwaling but it was so hard to get all the details. I would like to post code for web crawling, but it only can get `start time` and ` scores`. Also the page is quite simple so if you want to train your basic web crawling skill, then it will help.

``` python
import requests # from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime 
import time # import time -> time.sleep(5)
import re

# season 2018-2019
query = ['october', 'november', 'december', 'january', 'february', 'march']
v_name_list = []
v_score_list = []
h_name_list = []
h_score_list = []
time_list = []

for i in query : 
    url = "https://www.basketball-reference.com/leagues/NBA_2019_games-" + i + ".html"
    web = requests.get(url).content
    source = BeautifulSoup(web, 'html.parser')
    print (url)
    
    find_visitor = source.find_all('td', {'data-stat' : 'visitor_team_name'})
    find_v_score = source.find_all('td', {'data-stat' : 'visitor_pts'})
    find_home = source.find_all('td', {'data-stat' : 'home_team_name'})
    find_h_score = source.find_all('td', {'data-stat' : 'home_pts'})
    find_time = source.find_all('td', {'data-stat' : 'game_start_time'})
    
    for i in range(len(find_visitor)) :
        visitor_name =  find_visitor[i].text.strip().split('\n')[0]
        #print (visitor_name)
        v_name_list.append(visitor_name)
        v_score = find_v_score[i].text.strip().split('\n')[0]
        home_name = find_home[i].text.strip().split('\n')[0]
        h_score = find_h_score[i].text.strip().split('\n')[0]
        t_ime = find_time[i].text.strip().split('\n')[0]
    
        v_name_list.append(visitor_name)
        h_name_list.append(home_name)
        v_score_list.append(v_score)
        h_score_list.append(h_score)
        time_list.append(t_ime)
        
print ("finshed", len(v_name_list), len(h_name_list), len(v_score_list), len(h_score_list))

basket_df = pd.DataFrame({'Time':time_list, 'Home':h_name_list, 'Home_score':h_score_list, 'Visitor':v_name_list, 'Visitor_score':v_score_list})

#if you wnat to save as a csv file
#basket_df.to_csv('nba_project_rawdata.csv', encoding='utf-8')

basket_df[['home_int_score', 'visitor_int_score']] = basket_df[['Home_score','Visitor_score']].apply(pd.to_numeric)


basket_df['result'] = basket_df['home_int_score'] > basket_df['visitor_int_score']
basket_df.head()

del basket_df['home_int_score']
del basket_df['visitor_int_score']

basket_df
```

here is the output!

![output](/Users/soeunyi/Desktop/Screen Shot 2020-01-03 at 2.35.59 PM.png)



Web crawling is done for this, next time I am gonna start to do post processing with Kaggle data and training DL models.

