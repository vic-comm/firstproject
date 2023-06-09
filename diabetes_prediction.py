# -*- coding: utf-8 -*-
"""Diabetes prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mv0COCsgSlTszTbhiLq7dnNDq5_bXadd
"""

import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# loading the diabetes dataset to a pandas dataframe
diabetes_dataset = pd.read_csv('/diabetes.csv')

diabetes_dataset.head()

# nummber of rows and columns in this dataset
diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0--> Non-diabetic
1--> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# seperating data and labels
x = diabetes_dataset.drop(columns= 'Outcome', axis=1)
y = diabetes_dataset['Outcome']

print(x, y, sep='\n\n\n')

"""# **Data standardization**"""

scaler = StandardScaler()

scaler.fit(x)

standardized_data = scaler.transform(x)

print(standardized_data)

x = standardized_data
y = diabetes_dataset["Outcome"]

print(x, y, sep='\n\n')

"""train test split"""

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, stratify=y, random_state=2)

print(x.shape, x_test.shape, x_train.shape)

"""## **Training the model**"""

classifier = svm.SVC(kernel='linear')

# training the support vector machine classifier
classifier.fit(x_train, y_train)

"""## Model Evaluation

## Accuracy test
"""

# accuracy score from training data
x_train_prediction = classifier.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print("Accuracy score of training data : ", training_data_accuracy)

x_test_prediction = classifier.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
print("Accuracy score of training data : ", test_data_accuracy)

"""Making a predictive system"""

input_data = (1,89,66,23,94,28.1,0.167,21)

# changing the input data into a numpy array
input_data_as_numpy_array = np.array(input_data)

# reshape the array as we are predicting one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data  = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if prediction == [0]:
  print("Patient is not diabetic")
else:
  print("Patient is diabetic")

input_data = (6,148,72,35,0,33.6,0.627,50)

# changing the input data into a numpy array
input_data_as_numpy_array = np.array(input_data)

# reshape the array as we are predicting one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data  = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if prediction == [0]:
  print("Patient is not diabetic")
else:
  print("Patient is diabetic")





