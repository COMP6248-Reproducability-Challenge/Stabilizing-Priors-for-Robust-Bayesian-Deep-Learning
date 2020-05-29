# Stabilizing-Priors-for-Robust-Bayesian-Deep-Learning
## COMP6248 Deep Learning Reproducibility Challenge

This repository contains the codes and report for the reproducibility challenge of the paper - [Stabilizing Priors for Robust Bayesian Deep Learning](https://arxiv.org/abs/1910.10386) which was presented in Bayesian Deel Learning workshop at NeurIPS 2019.

The code for this challenge is based on [this original code](https://github.com/felixmcgregor/Bayesian-Neural-Networks-with-self-stabilising-priors/blob/master/BasicDemo.ipynb)

We have performed significant experimentation and analysis to replicate the results in a simple format.

### Installaion Instructions

It is recommedned to use the code files in Google Colab, as Bayesian models take time to train on the CPU. Use of GPU is highly recommended.

### Code File Description

* logger.py file is for creating the CSV files for training and test accuracy results.
* plotting.py file created by our group to plot the accuracy and loss results of the models.
* Prior stabilization vs BNN.ipynb notebook provides results for MNIST data and CIFAR10 dataset with prior stabilization.ipynb provides results for CIFAR10 data
