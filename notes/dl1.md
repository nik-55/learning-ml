```
input --> neural network ---> output
NLP ---> natural language processing

AI --> ML --> DL
ML mostly uses statistical techniques to find relation between input and output
DL depends on Logical structure called as neural network
This network is inspired from human brain

ANN ---> artificial neural network
Fundamental unit is called as perceptron
arrows are called as weights
layers

Types of neural network :
ANN RNN GAN CNN

In ML --> feature extraction ---> feature and labels

In DL ---> DL uses representational learning that automatically extract feature from raw data
Starting hidden layers extarct primitive feature and deep layer extract more complicated features

DL requires lot of data
it is said that ML wins with lesser data and after specific amount of data ML model performane remain still but deep
Learning algo performance keep growing with data

DL uses complex matrix multiplication
DL model run slow in CPU and require GPU
Training require lot of time sometime even months but ml model usually max to max an hour for training
Prediction time is lesser
DL model is not interpretable ---> do not come to know why it has produced that specific result

hardware ---> NPU TPU EdgeTPU FPGA
Pytorch by facebook
tensorflow by google

Architecture --> different neural network
which architecture to use?
experiments need to be conducted to find best suited architecture for a given problem

Image classification ---> ResNet architecture
Text classification ---> BERT architecture

MLP ---> multilayer perceptron
Input layer ---> hidden layers ---> output layers

CNN ---> convolutional ---> self driving

RNN ---> Recurrent
GAN ---> Generative Adversial Network

-------------------------------------------------

Perceptron is a algorithm which is used for supervised machine learning
We can call perceptron as a mathematical function

z = x1.w1 + x2.w2 + b.1
x1, x2 to sumation block is called as weight
1 to summation block is called as bias

z is sent to activation function
Activation is used to bring z in given range

Perceptron is only available to solve linear function and hence we use multilayer perceptron
MLP can solve non linear functions as well

Training is used to find w1, w2 and b

Geometric Intuition
Perceptron is called binary classifier
It is a line

Perceptron works on sort of linear data

To find the coffecients we first choice a random coefficients and form a line and then ask a random
points is the line classifying you correctly and then if point says yes so we move to next particle but if it
says no then we do some changes in previous cofficients and then continue this process of asking random points and modifying coefficients

changes in intercept moves line parallel to itself
change in a1 rotates the line about the point where x1 = 0

if line is to move towards positive then substract the (learning rate)*(coordinates of point, 1) from (coefficients of line)
if line is to move towards negative then add the (learning rate)*(coordinates of point, 1) to (coefficients of line)

epoch = 1000 , n(leraning rate) = 0.01
for i in range(epoch):
    randomly select a point
    if point belong to - and model predict pos :
        wnew = wold - n*point
        // w and point are matrix

    if point belong to + and model predict neg :
        wnew = wold + n*point
        // w and point are matrix

Now line may not be same when run multiple time as it's not finding minimum losses line

Perceptron Loss function


```
