# Master Thesis

## Introduction
This repository contains all the code concerning my Master Thesis on Convolutional Neural Architecture Search at ULB.

This thesis explores the Neural Architecture Search by Hillclimbing (NASH) [[arXiv]](https://arxiv.org/abs/1711.04528) algorithm for automatically designing architectures for Convolutional Neural Network. The NASH algorithm is a combination of the hillclimbing strategy, network morphisms [[arXiv]](https://arxiv.org/abs/1511.05641), and training via Stochastic Gradient Descent with warm Restarts (SGDR) [[arXiv]](https://arxiv.org/abs/1608.03983). The aim of the experiments was to find the best combination of hyperparameters, study the effect of incorporating dropout and early stopping techniques on the performance and computational cost of the models and study the effect of the network morphisms in our methods. The experiments were conducted on three different datasets, namely CIFAR-10, CIFAR-100, and SVHN.
