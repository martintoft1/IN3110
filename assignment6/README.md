# Assignment 6

### Prerequisites

In order to run the code from the tasks in this assignment, the user needs to install the packages described in requirements.txt. These packages can be installed from the terminal by first moving to the folder where requirements.txt is located, and then writing

```
python3 -m pip install -r requirements.txt
```

### Tests

All of the tests for this assignment is located in the test_webprogramming.py-file, and can be run from the terminal by first moving to the folder where the file is located, and then writing

```
py.test
```

## Task 6.1

### Functionality

In this task we were tasked to make the file webvisualization_plots.py which contains the functions "get_data_from_csv", "plot_reported_cases_per_million", along with a function "main". The get_data_from_csv-function creates a pandas dataframe from a .csv-file, containing data about covid-cases per million from given countries over a given timeframe. The plot_reported_cases_per_million-function uses the get_data_from_csv-function to create a dataframe, and then creates a plot and displays the plot to the user. The main-function takes user-input, and use the input as arguments for the plot_reported_cases_per_million-function. 

### Usage

To get data from csv, the user needs to run the following command in python

```python
get_data_from_csv(columns, countries, start, end)
```

where
- columns is a list of the columns you want to extract information about, along with the default columns "location" and "date" 
- countries is a list of the countries you want to extract information about
- start and end respectively are the start- and end-dates of the timeframe that information is to be extracted for, written on the format YYYY-MM-DD

To plot the data, the user needs to run the following command in python

```python
plot_reported_cases_per_million(countries, start, end)
```

where the arguments are exactly the same as the arguments with the same name in the get_data_from_csv-function.

To run main, the used needs to run the following command from the terminal

```
python3 webvisualization_plots.py
```

and follow the instructions printed to the terminal.


## Task 6.2

### Functionality
In this task we were tasked to make the file webvisualization.py. This file builds a FastAPI-app which uses the script webvisualization_plots.py to generate a plot of covid cases, and displays the plot on a webpage.

### Usage
To display the plot on a webpage, the user needs to run the following command from the terminal

```
python3 webvisualization.py
```

To see the plot, the user can then visit the url stated in the terminal.


## Task 6.3

### Functionality
In this task we were tasked to build on the functionality from 6.2, adding the posibility for selecting countries, start-date and end-date on the webpage, and update the plot with the press of a button. 

### Usage
Same as 6.2.
