<!-- [![DOI](https://zenodo.org/badge/[doi].svg)](https://zenodo.org/badge/latestdoi/[doi]) -->

# PyTorch Tutorial 2022

## Installation

**As an alternative to local installation, the notebooks can be used via Google Collab**

Minimum python version is 3.8. Recommend creating a virtual environment, e.g. assuming your are using [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html) (if installing conda for the first time, remember to restart the shell before attemting to use conda, and that by default conda writes the setup commands to `.bashrc`):

```
conda activate root
conda install nb_conda_kernels
conda env create -f environment.yml
conda activate pytorch_tutorial_2022
```

Otherwise set up a suitable environment using your python distribution of choice using the contents of `environment.yml`. Remember to activate the correct environment each time, via e.g. `conda activate pytorch_tutorial_2022`.

Install dependencies

```
pip install -r requirements.txt
```

## Tutorial parts

The tutorial is split into several sections, most of which are followed by exercises that draw on the items covered in the  related section. Exercises also have corresponding answer versions of the notebooks, but I'd advise giving the questions a good attempt first.

1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/00_Tensors.ipynb) 00 Tensors: Covers the fundamental data storage class in PyTorch, and how tensors can be manipulated and interacted with
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/00_Tensors_exercises.ipynb) Exercises
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/00_Tensors_exercises_answers.ipynb) Answers
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/01_autograd.ipynb) 01 Autograd: Covers how tensors can be differentiated
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/01_autograd_exercises.ipynb) Exercises
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/01_autograd_exercises_answers.ipynb) Answers
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/02_distributions.ipynb) 02 Distributions: Covers how to build (differentiable) distributions and sample from them
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/02_distributions_exercises.ipynb) Exercises
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/02_distributions_exercises_answers.ipynb) Answers
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/03_nn-Module.ipynb) 03 NN Modules: Covers the fundamental class for implementing neural networks
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/03_nn-Module_exercises.ipynb) Exercises
    - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/03_nn-Module_exercises_answers.ipynb) Answers
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/04_losses.ipynb) 04 Loss functions: How to differentiably score the performance of networks
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/05_optimisers.ipynb) 05 Optimisers: Intro to creating optimisers and how to update network parameters via gradient descent
1. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GilesStrong/pytorch_tutorial_2022/blob/main/notebooks/06_neural_network.ipynb) 06 Neural Networks: How to construct a simple training loop for optimising a DNN
