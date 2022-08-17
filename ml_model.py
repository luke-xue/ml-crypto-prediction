import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

from sentiment_analysis import sentiment_analysis

df = sentiment_analysis("2022-08-01", "2022-08-10")

input = df[["polarity"]]
output = df[["binary_change"]]

input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=.2)

model = Sequential()
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(metrics='accuracy', loss='binary_crossentropy', optimizer='sgd')

model.fit(input_train, output_train, epochs=200, batch_size=15)

# y_hat = model.predict(input_test)
# y_hat = [0 if val < 0.5 else 1 for val in y_hat]

# print(input_test, output_test, y_hat)


df2 = sentiment_analysis("2022-08-15", "2022-08-16")
input = df2[["polarity"]]
y_hat = model.predict(input)

print(y_hat)