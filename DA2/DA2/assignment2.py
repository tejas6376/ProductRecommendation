# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H8FwM9S8FLNuPrOQ_9gE5MKGsMtHAJ7W
"""

# Task 1: Read the dataset and do data pre-processing
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
data = pd.read_csv("drug200.csv")
features = data.drop("Drug", axis=1)
labels = data["Drug"]
encoder = LabelEncoder()
features["Sex"] = encoder.fit_transform(features["Sex"])
features["BP"] = encoder.fit_transform(features["BP"])
features["Cholesterol"] = encoder.fit_transform(features["Cholesterol"])
classencoder = LabelEncoder()
labels = classencoder.fit_transform(labels)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Task 2: Build the ANN model with (input layer, min 3 hidden layers & output layer)
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=scaled_features.shape[1]))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=5, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(scaled_features, labels, epochs=100, batch_size=32, validation_split=0.2)

# Task 3: Test the model with random data
import warnings
warnings.filterwarnings("ignore")
import random
def generate_random_data():
    age_range = (18, 65)
    sexes = ['F', 'M']
    bps = ['LOW', 'NORMAL', 'HIGH']
    cholesterols = ['NORMAL', 'HIGH']
    na_to_k_range = (0, 30)
    age = random.randint(age_range[0], age_range[1])
    sex = random.choice(sexes)
    bp = random.choice(bps)
    cholesterol = random.choice(cholesterols)
    na_to_k = round(random.uniform(na_to_k_range[0], na_to_k_range[1]), 3)
    return age, sex, bp, cholesterol, na_to_k
df = pd.DataFrame(columns=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])
num_instances = 100
for _ in range(num_instances):
    data = generate_random_data()
    df = df.append(pd.Series(data, index=df.columns), ignore_index=True)
df["Sex"] = encoder.fit_transform(df["Sex"])
df["BP"] = encoder.fit_transform(df["BP"])
df["Cholesterol"] = encoder.fit_transform(df["Cholesterol"])
random_data = scaler.fit_transform(df)
predictions = model.predict(random_data)
predicted_labels = predictions.argmax(axis=1)
predicted_drugs = classencoder.inverse_transform(predicted_labels)
print("Random Data:")
print(df)
print("Predicted Drug class:")
print(predicted_drugs)