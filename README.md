<!-- [![DOI](https://zenodo.org/badge/[doi].svg)](https://zenodo.org/badge/latestdoi/[doi]) -->

# PyTorch Tutorial 2022

## Installation

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