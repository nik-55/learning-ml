# 1> import the data
# data need to be in .csv

# 2> clean the data
# there may be some empty field 

# 3> Split the data into training/test sets
# Let we train our ML model with 80% of avalaible data and then test
# our model against the remaining 20% of data 
# Features are input to the ML model And Labels are output
# We will first train our ML model by telling it that these are features 
# and these are its corresponding labels by using 80% of data
# Then we will input features from remaining 20% data and test if our model 
# gives the correct label or not

# 4> Create a Model

# 5> Train the model

# 6> Make Predictions

# 7> Evaluate and improve

# --------------------------------------------------------

# Libraries ==== Numpy , Pandas , Scikit-Learn 
# Download Anconda which will install jupyter Notebook 

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

# music_data = pd.read_csv('music.csv')
# music.csv is like excel that have columns age , gender , genre
# age,gender === feature 
# genre === label

# x = music_data.drop(columns=["genre"])  
# y = music_data["genre"]

# x === feature
# y === label

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

# model = DecisionTreeClassifier()
# model.fit(x_train,y_train)

# predictions1 = model.predict(x_test)

## predictions2 = model.predict([[21,1],[22,0]])
## 1 === Male , 0 === Female 
## 21,22 === age