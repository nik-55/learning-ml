features ---> input
label ---> output
datasets ---> Uci ml repo or kaggle

ML is of two types

1. Supervised Learning :
   a. classification : span or not spam (classifier)
   b. regression : house price predictor (regressor)

Already tagged data
Features and labels present

Linear regression
decision tree classifier
random tree classifier
random forest regressor

2. Unsupervised Learning :
   a. clustering : grouping in the data such as grouping customers by purchasing behavior
   b. Association : people who buy shoes tends to buy socks

Data not already tagged
features and labels not present
training not done

scikit learn ---> ml library
independent --> features
dependent --> labels

Regressor --->
simple linear regression tries to fit data in a line that gives minimum losses
f(x) = w0 + w1x1 + w2x2 + w3x3
x1, x2, x3, x4 are independent and called as features
f(x) is called as label
w0, w1, w2, w3, w4 are weights
ml model tries to find the best weight and then learn it and if we give them new
feature they simply apply above equation with their learned weights
Model Training is to find these weights

there are many loss functions like :
mean squared error
absolute error
sum squared error

partial differentiating these losses with respect to each feature and equating each
differentiation to zero we can find weights
however we have so many features and solving these equation become very tough
exact methods are computationally expensive so we use -->

> gradient descent

`xnew = x - Lr*(dy/dx)`
Lr ---> learning rate
assuming w0,w1,w2...wn and replace using above and finally converge to point where loss is minimum

batch size = all the data at once --> gradient descent

batch size = 1 so called stochastic gradient descent

Mini batch Gradient descent
batches of like 1000 size is created from million of data and is used for gradient descent

classifier -->
Model training draws a boundary line
then whenever new data come if it lies on one side then it is spam and if it lies on another
side then it is not spam

decision tree ---> forms binary tree type questions on training

k nearest neighbor ---> among k nearest neighbors if there are more number of spam neigbor then it is spam otherwise it is not spam
As distances are calculated at prediction and there is nothing in name of training --> cons

> evaluating the model

to solve overfitting use

1. cross validation
2. holding a validation dataset

sometime it happens that model just learn its training data and hence it gives zero losses when testing with one combination of train data
however when such model recieves different combination of train data its predictions may be very much wrong

Logestic regression is a classifier!!
it calculates probability and hence called as regression
we can set 0.5 as cutoff and therefore we can tell rain or not rain
hence it works as classifier

sigmoid function ---> probability ---> `1/{1+e^(-y)}`
odds in probability = `p/(1-p)`
log(odds) = y --> w0 + w1x1 + w2x2 + w3x3 = linear regression
but in logestic regression loss function is not mean squared error
we will use log loss
loss = -ylog(y') - (1-y)log(1-y')
now find the weights of linear regression minimizing this loss function
