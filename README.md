## Overview

This is the repository containing program to calculate the rotational energy levels and eigenvectors for asymmetric top molecules. Program is a part of Masters Degree Thesis conducted on Gdańsk University of Technology. 

## Getting started 

**Cloning the repository**

To clone this repository run one of this command into your terminal. If you have assigned an SSH key to your GitHub account try:
```bash
git clone ...
```
and if you haven't, use HTTP (this will recquire logging):
```bash
git clone ...
```

**Setting up the virtual environment**

To setup the virtual enivornment you should first acquire the venv package by running:
```bash
sudo apt install python3-venv
```

then, to crate virtual environment, from the root of this repository run:
```bash
python3 -m venv env
```

and then to activate it:
```bash
source env/bin/activate
```

When you want to terminate your virtual environment just type:
```bash
deactivate
```

**Downloading packages**

With active virtual enivironment run following command to download all the recquired packages for program to operate:
```bash
pip install -r requirements.txt
```
