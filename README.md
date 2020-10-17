# Web-scrapper

The purpose of this project is to build a small web-scrapper for the subject "Data tipology and lifecycle" from UOC.
This web-scrapper parses a given website looking for anchor tags to later on store the products catalog data in a
pandas dataframe  


## Authors
  [Victor Morant](https://github.com/vmorant)  
  [Aitor Jara](https://github.com/A3itor)  


## Getting Started

These instructions will get us a copy of the project up and running on our local machine.
In case that we are not using an IDE like Pycharm, that automatically sets a virtual environment up for us, we will need to set it up by ourselves, by typing the following command on a terminal:
```
python3 -m venv scrapper
```
This will create a virtual environment called "scrapper" on our local machine, in the current directory.
Next we will activate the virtual environment, with the following command:
```
source scrapper/bin/activate
```
Because we just created this virtual environment, it is empty and we need to install the dependencies (libraries) that the software needs to run correctly.
To do that we just run the following command:
```
pip install -r requirements.txt
```
Now, in order to run this package we simply need to run the main.py file with the following command:
```
python3 main.py
```

Now, the main.py file has some options based on preferences:
We can assign different variables to the parameters <X, X1, X2, X3>
based on the output that we want to be displayed on the terminal. The output will be the result of one or more data pre-processing steps,
that will be initialized on demand at execution time, with the use of flags.

### Use of flags:
PENDIENTE


## Structure of the repository
PENDIENTE


## The dataset

The dataset is structured file on csv that contains a list of items extracted from the url. This file content a head with describe the information content in the fields.  