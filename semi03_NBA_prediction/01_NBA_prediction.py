#I put lots of comments in here, so I am barely sure you could understand easily,
#what I am trying to say :)

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import OneHotEncoder
from sklearn import model_selection

import tensorflow as tf
from tensorflow.keras import datasets, utils
from tensorflow.keras import models, layers, activations, initializers, losses, optimizers, metrics

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#this is the dataset from kaggle
df = pd.read_csv('./nba.games.stats_raw.csv') #you could change the name of dataset
data = pd.DataFrame(df) # make the dataset to dataframe ( to pandas data )

# we decided to use only season 17 -18, so needed to divide the dataset.


data['new_dates'] = pd.to_datetime(data['Date']) #so I copied Date column, and made a new column.
start_date = '10/01/2017' # picked the dates when I need (start / end)
end_date = '04/30/2018'
mask = (data['new_dates'] > start_date) & (data['new_dates'] <= end_date) #make the mask like using as a filter.
data = data.loc[mask] # asjust the mask, and we are going to use only 17-18 season's data
#data.head() # you check the new_dates column are only have 17-18

# we are going to change the type of dataset text to numeric.
# for example, the team is Home -> 1 / Away -> 0

arrange = [data]
for dataset in arrange :
    dataset.loc[dataset['Home'] == 'Home', 'Home'] = 1
    dataset.loc[dataset['Home'] == 'Away', 'Home'] = 0
#data['Home'].head() # adjust the changing to 'Home'column then you could see the changing.

for dataset in arrange:
    dataset.loc[dataset['WINorLOSS'] == 'W', 'WINorLOSS'] = 1
    dataset.loc[dataset['WINorLOSS'] == 'L', 'WINorLOSS'] = 0
#data['WINorLOSS'].head()

# our project's goal is result prediction of NBA so split the 'WINorLOSS' column as a target data.
# Besides from target data then
x_data = data
y_data = x_data[['WINorLOSS']]

# delete the columns that looks useless for now.
del data['WINorLOSS']
del data['new_dates'] # we already used this coulmn as a filter.
del data['Unnamed: 0']
del data['Date']
del data['Game']
del data['TeamPoints']
del data['OpponentPoints']
#data.info()

# #trying to change the string data to integer but this process was not improve any of results
# #we did it, but just do it just in case so you also have check this part.
# df_team = data['Team']
# df_team2 = df_team.drop_duplicates(keep='first')
# df_team2
# da = [data]
# team_titles = {"ATL": 1, "BOS": 2, "BRK": 3, "CHO": 4, "CHI": 5,
#                "CLE": 6, "DAL": 7, "DEN": 8, "DET": 9, "GSW": 10,
#               "HOU": 11, "IND": 12, "LAC": 13, "LAL": 14, "MEM": 15,
#               "MIA": 16, "MIL": 17, "MIN": 18, "NOP": 19, "NYK" :20,
#               "OKC": 21, "ORL": 22, "PHI": 23, "PHO": 24, "POR": 25,
#               "SAC": 26, "SAS": 27, "TOR":  28, "UTA": 29, "WAS": 30}

# for dataset in da:
#     dataset['Team'] = dataset['Team'].map(team_titles)
#     dataset['Opponent'] = dataset['Opponent'].map(team_titles)

# standardization, actually we skipped this at first but the result was not enough
# so we got the maximum amount then divided every column with own max.
target_col=['FieldGoals', 'FieldGoalsAttempted', 'FieldGoals.'
                 , 'X3PointShots','X3PointShotsAttempted', 'X3PointShots.' ,'FreeThrows',
                 'FreeThrowsAttempted', 'FreeThrows.', 'OffRebounds',
                 'TotalRebounds', 'Assists', 'Steals', 'Blocks', 'Turnovers', 'TotalFouls',
                'Opp.FieldGoals', 'Opp.FieldGoalsAttempted', 'Opp.FieldGoals.' ,'Opp.3PointShots',
                 'Opp.3PointShotsAttempted', 'Opp.3PointShots.' ,'Opp.FreeThrows',
                 'Opp.FreeThrowsAttempted',
                'Opp.OffRebounds', 'Opp.TotalRebounds', 'Opp.Assists', 'Opp.Steals', 'Opp.Blocks',
                'Opp.Turnovers', 'Opp.TotalFouls']
weight_col = data[target_col].max() #get the maxium
data_norm = data[target_col]/weight_col # nomalization (standardization)
data = data_norm
#data_norm.info()

#keras
x_data = data

train_data, test_data, train_label, test_label = model_selection.train_test_split(x_data, y_data, test_size=0.3, random_state=0)

print("train_data:", train_data.shape)
print("test_data:", test_data.shape)
print("train_label:", train_label.shape)
print("test_label:",test_label.shape)


enc = OneHotEncoder(categories='auto')

enc.fit(train_label)
train_label = enc.transform(train_label).toarray()

enc.fit(test_label)
test_label = enc.transform(test_label).toarray()

print("after OneHotEncoder train_label:", train_label.shape)
print("after OneHotEncoder test_label:", test_label.shape)


tf.logging.set_verbosity(tf.logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # https://stackoverflow.com/questions/35911252/disable-tensorflow-debugging-information

model = models.Sequential()

model.add(layers.Dense(input_dim=31, units=128, activation=None, kernel_initializer=initializers.he_uniform()))
model.add(layers.BatchNormalization()) # Use this line as if needed
model.add(layers.Activation('elu')) # layers.ELU or layers.LeakyReLU

model.add(layers.Dense(units=256, activation=None, kernel_initializer=initializers.he_uniform()))
model.add(layers.BatchNormalization())
model.add(layers.Activation('elu'))

model.add(layers.Dense(units=256, activation=None, kernel_initializer=initializers.he_uniform()))
model.add(layers.BatchNormalization())
model.add(layers.Activation('elu'))
model.add(layers.Dropout(rate=0.3))

model.add(layers.Dense(units=128, activation=None, kernel_initializer=initializers.he_uniform()))
model.add(layers.BatchNormalization())
model.add(layers.Activation('elu'))

model.add(layers.Dense(units=2, activation='softmax')) # One-hot vector for 0 & 1

model.compile(optimizer=optimizers.Adam(),
              loss=losses.categorical_crossentropy,
              metrics=[metrics.categorical_accuracy])

history = model.fit(train_data, train_label, batch_size=100, epochs=20, validation_split=0.3)
result = model.evaluate(test_data, test_label, batch_size=100)

print('loss (cross-entropy) :', result[0])
print('test accuracy :', result[1])

val_acc = history.history['val_categorical_accuracy']
acc = history.history['categorical_accuracy']


x_len = np.arange(len(acc))
plt.plot(x_len, acc, marker='.', c='blue', label="Train-set Acc.")
plt.plot(x_len, val_acc, marker='.', c='red', label="Validation-set Acc.")

plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('Accuracy')
plt.show()
