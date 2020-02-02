# NBA game prediction

semi project part3.

> This project is just part of my practice, so something went wrong and looks like amateur, it's alright! I am sure I am getting better and better and that is my goal :)

* We were looking for something fun to use data and some models for ML/DL.

- Got the data from kaggle (https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018)
- Actually we were trying to use web crwaling but it was so hard to get all the details. I would like to use my code for web crawling, but it only can get `start time` and ` scores`. Also the page is quite simple so if you want to train your basic web crawling skill, then it will help.
- When you check the my crawling code, then you will find out which web page that I use for crawling.



## DATA

Here is the data that we used for our project. When you sign up to Keggle, then you could download it easily. The link below, you can find the example of this dataset.

-  https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018



## What for

We got the assignment to use `pandas` and `ML / DL algorithm` for practice, so It could be not meaningful at all but we were trying to use all the skill that we learned from the class. I guess that is the purpose of this assignment. Also It was a really great chance to review.



Also, We have tried to select a few column to train the models, but it couldn't get meaningful results. After several tries then we just figured out put all the data to train then it works! It could be overfitted a lot, However this is just meaningful we did it!



## Suggestion

When I was post processing the dataset, and just right before put the data in to train, I was struggling from the type. Because I needed `inteager` data, but the data that changed text to numeric was `object` type, so It kept saying the shape didn't fit. So I did change the type from `object` to `numeric`.

I guess the whole code doesn't include this part, because my team mates don't need this process. Anyway, I just want to put this one in here just in case for who are suffering with same problem with me. You can easily use `pd.to_numeric`.

```shell
x_data['int_home'] = x_data['int_home'].apply(pd.to_numeric, errors='coerce')
y_data['int_win_loss'] = y_data['int_win_loss'].apply(pd.to_numeric, errors='coerce')

# get the column that need to be changed the type first, then you can easily change with 'pd.to_numeric'
```







