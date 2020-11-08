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


### Use of flags:
With can use flags to control the important parameters of the web-crawler, such as the number of links to retrieve or the starter url
at execution time, without changing the code, which is pretty convenient:

We might run:\
```python3 main.py --url https://www.tuaceitedemotor.com```\
```python3 main.py -u https://www.tuaceitedemotor.com```(simplified flag)

Or:\
```python3 main.py --num_links 10```\
```python3 main.py -n 10```(simplified flag)

We might even run the two of them simultaneously:\
```python3 main.py -u https://www.tuaceitedemotor.com -n 10```


## Structure of the repository
The package consists of two core files: "webscrapping.py" and "main.py", which instantiate and execute the WebScrapper class that parses the webcontent and generates a data.csv file.

The data folder contains the data.csv generated file along with a screenshot of the dataframe at acquisition time.

Finally there is the "requirements.txt" file previously mentioned to set up a virtual environment.


## The dataset

The dataset is structured file on csv that contains a list of items extracted from the url. This file content a head with describe the information content in the fields.  