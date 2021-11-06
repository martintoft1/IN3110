# Assignment 5

## Task 5.1

### Prerequisites
In order to run the code from this task and the following tasks, the user needs to install the packages described in requirements.txt. These packages can be installed from the terminal by first moving to the folder where requirements.txt is located, and then writing

```
python3 -m pip install -r requirements.txt
```

### Functionality
In this task we were tasked to make the file requesting_urls.py which contains the function get_html. The function gets the entire html source-file or part of it from a given webpage as a string. The function also gives the user the option of writing the html source-file to a .txt-file located in the requesting_urls-folder.

### Usage
To get the html source-file as a string, the user needs to run the following command in python

```python
get_html(url, params, output)
```

where params is the optional parameters for getting only parts of the html source-file, and output is the optional name of the txt-file that the html source-file string is to be written to. 

## Task 5.2

### Prerequisites
Read Prerequisites in Task 5.1.

### Functionality
In this task we were tasked to make the file filter_urls.py which contains the functions find_urls and find_articles. The find_urls-function finds and returns a list with all the urls from a html source-file. The find_articles-function uses the find_urls-function, and then finds and returns a list with all the wikipedia-article-urls from the list of urls. Both the functions also gives the user the option of writing the lists to .txt-files located in the filter_urls-folder.

### Usage
To get all the urls from a html string, the user needs to run the following command in python

```python
find_urls(html_str, base_url, output)
```

where html_str is the html string, base_url is the url prior to the relative urls in the html-string (prior to the first / character following the .com, .no or similar), and output is the optional name of the txt-file that the urls are to be written to. 

To get all the articles from a wikipedia-page, the user needs to run the following command in python

```python
find_articles(url, output)
```

where url is the url of the wikipedia-page, and output is the optional name of the txt-file that the articles are to be written to. 

## Task 5.3

### Prerequisites
Read Prerequisites in Task 5.1.

### Functionality
In this task we were tasked to make the file collect_dates.py which contains the function find_dates. The find_dates-function finds and returns a list with all the dates from a webpage in sorted order. The function also gives the user the option of writing the lists to .txt-files located in the collect_dates_regex-folder.

### Usage
To get all the dates from a webpage, the user needs to run the following command in python

```python
find_dates(url, output)
```

where url is the url of the page that is scanned for dates, and output is the optional name of the txt-file that the dates are to be written to. 

## Task 5.4

### Prerequisites
Read Prerequisites in Task 5.1.

### Functionality
In this task we were tasked to make the file time_planner.py which contains the functions extract_events and create_betting_slip. The time_planner-function finds and returns a list with all the events from a wikipedia-page for the 2021–22 FIS Alpine Ski World Cup, and potentially other wikipedia-pages with events if they follow the same format. The create_betting_slip-function saves a markdown betting slip produced with data from a set of events.

### Usage
To get the events from the webpage(s), the user needs to run the following command in python

```python
time_planner(url)
```

where url is the url of the page that is scanned for events.

To make the betting slip for a set of events, the user need to run the following command in python

```python
create_betting_slip(events, save_as)
```

where events is the events, and save_as is the name of the .md-file.

## Task 5.5

### Prerequisites
Read Prerequisites in Task 5.1.

### Functionality
In this task we were tasked to make the file fetch_player_statistics.py which contains different functions, all used in the find_top_three_each_team-function. This function takes in the url of the wikipedia-page containing the bracket for the NBA Playoffs 2021. The function then extracts the players of the teams that made it to the conference semifinals, calculates the top three players for three different statistics in the NBA season, makes plots for the different statistics for all the teams, and returns the lists conctaining the top three. The three statistics mentioned is points per game (ppg), blocks per game (bpg), and rebounds per game (rpg).

### Usage
To find the top three for each statistic and each team, the user needs to run the following command in python

```python
find_top_three_each_team(url)
```

where url is the url of the wikipedia-page for the NBA Playoffs 2021.

## Tests

### Prerequisites
Read Prerequisites in Task 5.1.

### Functionaliry
Tests all the functionality implemeted in the different tasks in assignment 5.

### Usage
To test all the functions and methods from the assignment, the user needs to run the following command from the assignment5-directory

```
py.test
```