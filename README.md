# Neural-Style-Transfer
## Overview

Neural style transfer is a way to make new images by combining the content of one image with
the style of another image. The process requires a lot of computing power, and putting the model
on a web server can be hard because the inference time can slow down service to users. The aim
of this project is to deploy neural style transfer on a web server written in Streamlit. We have
built a web-based app for Neural Style Transfer based on the model proposed by Perceptual Losses
for Real-Time Style Transfer and Super-Resolution Perceptual Losses for Real-Time Style Transfer
and Super-Resolution.

**The model is basically divided into 2 parts, one of which is an Image Transformation Network, and the other one is a Loss Network.**

![image](https://github.com/HarshithK13/Neural-Style-Transfer/assets/84466567/c04c78a9-ed2f-4c29-9b90-f07600e8f10b)

## Image Transformation Net

The basic idea behind an image transformation network is to train a neural network to take an
input image and generate a transformed version of that image.

In style transfer tasks, the network consists of two parts: an encoder that extracts content infor-
mation from the input image and a decoder that synthesizes the transformed image based on the

style information. The Image Transformation Network is a Convolutional Neural Network with
deep residual connections. The weights of this network ($W$) are learned by calculating losses using
the output image ($\hat y$) and comparing them with: - the representations of the style image ($y_s$) and
content image ($y_c$).

## Loss Network

A loss network, also known as a feature extraction network or a perceptual network, is an essential
component of the algorithm. It plays a crucial role in computing the loss function used to optimize
the generated stylized image. The loss network is typically a pre-trained convolutional neural
network (CNN). The Loss Network we have used here is VGG16 that has already been trained on
the ImageNet Dataset.

The loss network is used to get representations of content and style from images of content and
style:

(i) The information representations come from the relu(3,3) layer.

(ii) The style models come from the layers relu(1,2), relu(2,2), relu(3,3), and relu(4,3).
The intermediate feature maps, typically obtained from different layers of the CNN, capture the
content and style information of the input images. By comparing these feature representations, the
loss network enables the algorithm to optimize the generated image to match the content and style
characteristics of the input images.


**Feature Reconstruction Loss**

Feature Reconstruction Loss focuses on matching the intermediate feature representations of the
generated image with those of the style image.

The Feature Reconstruction Loss is the (squared, normalized) Euclidean distance between two
feature representations.

![image](https://github.com/HarshithK13/Neural-Style-Transfer/assets/84466567/b78b383d-4e66-4d1b-9313-f235c18cd2ad)

**Style Reconstruction Loss**

With the output image ($\hat y$) and the style representations from the layers relu(1,2), relu(2,2), relu(3,3)
and relu(4,3) and using the following loss function from the image First we define Gram matrix $G^φ_j(x) as $C_jC_j$ whose elements are:

![image](https://github.com/HarshithK13/Neural-Style-Transfer/assets/84466567/bf08d877-e03e-42dc-8be7-8f80ef84a5a4)

This matrix tries to capture corellation across the channels.

The style reconstruction loss is then the squared Frobenius norm of the difference between the
Gram matrices of the result image and the target image.

![image](https://github.com/HarshithK13/Neural-Style-Transfer/assets/84466567/ed921b20-4a10-4328-932d-e76f02abca53)

## Sample Outputs

We have deployed the app with the help of Streamlit. This app takes in an image as input. Then,
we are given a few names to select from which depict the style which is going to be implemented.
On selection of the style, we click the button which says ”Stylize” and then we get the output image
which is the stylized version of the input image.

![image](https://github.com/HarshithK13/Neural-Style-Transfer/assets/84466567/ba82f856-da79-47c7-8d9c-a09f3154f8f3)

## Resources

1. https://github.com/pytorch/examples/tree/main/fast_neural_style
2. https://arxiv.org/pdf/1603.08155.pdf

