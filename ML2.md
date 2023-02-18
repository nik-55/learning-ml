> uci data set respository

`reading the csv file and have look on data
try to deal in numbers only`

> plot the graphs to analysis the data

> Test train splitting

> Looking for correlations

> Trying out different combinations

> Deal with missing attributes

> Feature scaling

> Pipeline

> Selecting the model

```
model = LinearRegression()
model.fit(features,labels)
```

> Evaluating the model again on train_features

```
predictions = model.predict(train_features)
mse = mean_squared_error(train_labels,predictions)
rmse = np.sqrt(mse)
```

> Cross validation

```
If model overfits the dataset
scores = cross_val_score(model,features,housing_labels,scoring="neg_mean_squared_error",cv=10)

rmse_scores = np.sqrt(-scores)
```

> dumping the model

`dump(model,'Dragon.joblib')`

> testing the data with test_features

> modal usage

`model = load('Dragon.joblib')`
