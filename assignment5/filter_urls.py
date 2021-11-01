# Import necessary modules
from requesting_urls import get_html  
import os
import re  # Regex


def find_urls(html_str, base_url=None, output=None):
    """
    Finds and returns a list with all the urls from a html source-file

    Args:
        html_str (str): String containing a html source-file
        base_url (str): The base-url of the webpage that the html source-file was taken from, that is to be combined with the relative urls found in the file
        output (str): Name of the txt-file that the list of urls should be written to
    Returns:
        urls (list): A list containing all the urls found in the html-string
    """
    # Regex-pattern for finding all the absolute urls 
        # The url-regex-pattern matches a string that start with 'href="'. 
        # The string should then be followed by any group of characters that doesn't contain a hashtag, i.e fragment identifiers, and doesn't contain any whitespace-characters. 
        # The string should finish with the caracter ". 
        # The pattern only returns the content between the delimeters.
        # The pattern does not remove the comments, this needs to be done after finding the relative urls
    abs_url_pat = re.compile(r'(?<=href=")(?:https?://)[^"]+(?=")')

    # Regex-pattern for finding all the relative urls, as well as the urls that don't require HTTP-protocol
        # The regex-pattern matches a string that start with 'href="'. 
        # The string should then be followed by any group of characters that doesn't start with a hashtag, i.e fragment identifiers, and doesn't contain semicolons or quotation marks. 
        # The string should finish with a quotation mark. 
        # The pattern only returns the content between the delimeters, i.e. the quotation marks.
        # The content that is returned also contains in-line comments from the source-file, so these needs to be removed after finding the relative urls
    rel_url_pat = re.compile(r'(?<=href=")[^#]{1}[^"|:]+(?=")')
    
    # Find urls from the html source-file that match with the regex-patterns 

    # *** Absolute urls ***
    # Find the urls
    abs_urls = re.findall(abs_url_pat, html_str)
    # Strip the urls for comments
    i = 0
    for url in abs_urls:
        # Strip for comments
        if '#' in url:
            abs_urls[i] = abs_urls[i].split('#', 1)[0]
        i+=1

    # *** Relative urls *** 
    # Find the urls
    rel_urls = re.findall(rel_url_pat, html_str)
    # Strip the urls for comments, as well as combine the relative urls with the base url if given
    i = 0
    for url in rel_urls:
        # Strip for comments
        if '#' in url:
            rel_urls[i] = rel_urls[i].split('#', 1)[0]
        # Merge with base url, unless the relative url starts with // - then only strip the url of these characters
        if '//' in url:
            rel_urls[i] = rel_urls[i].strip('//')
        else:
            if base_url:
                rel_urls[i] = base_url + rel_urls[i]
        # Increase count
        i+=1

    # Merge the lists with urls
    urls = abs_urls + rel_urls

    # Check if the output-argument was given; if so, write to file with name "<output>_urls.txt" 
    # in the "filter_urls"-directory
    if output:
        # Create urls-string 
        urls_str = ""
        for url in urls:
            urls_str += url + "\n"

        # Write to file
        # Save current directory
        path = os.getcwd()
        # Switch to "filter_urls"-directory and write to file
        os.chdir("filter_urls")
        f = open(output + "_urls.txt", "w")
        f.write(urls_str)
        f.close()
        # Change back to the current directory
        os.chdir(path)
   
    return urls


def find_articles(url, output=None):
    """
    Finds and returns a list consisting only of urls to Wikipedia-articles, from a list of urls

    Args:
        url (str): The url of the wikipedia-page that is to be scanned for articles
        output (str): Part of the name of the txt-file that the list of urls and articles should be written to
    Returns:
        articles (list): A list containing the urls of all the articles found in the html-string
    """
    # Get html-string from url
    html_str = get_html(url)

    # Find base-url from url
    # The base-url-pattern matches with urls that start with 
    base_url_pat = re.compile(f'(?:https?://)[^/]+')
    match = re.search(base_url_pat, url)
    base_url = match.group()
    print(base_url)

    # Find all urls from wikipedia-page
    urls = find_urls(html_str, base_url, output)

    # Find articles from urls
    articles = []
    for url in urls:
        if 'wikipedia' in url:
            articles.append(url)

    # Check if the output-argument was given; if so, write to file with name "<output>_articles.txt" 
    # in the "filter_urls"-directory
    if output:
        # Create articles-string 
        articles_str = ""
        for url in articles:
            articles_str += url + "\n"

        # Write to file
        # Save current directory
        path = os.getcwd()
        # Switch to "filter_urls"-directory and write to file
        os.chdir("filter_urls")
        f = open(output + "_articles.txt", "w")
        f.write(articles_str)
        f.close()
        # Change back to the current directory
        os.chdir(path)

    return articles


# Tests to see if the find_urls-function works correctly
def test_find_urls():
    # Get urls from Nobel_Prize-page
    html = get_html("https://en.wikipedia.org/wiki/Nobel_Prize")
    find_urls(html, base_url="https://en.wikipedia.org", output="Nobel_Prize")

    # Get urls from Bundesliga-page
    html = get_html("https://en.wikipedia.org/wiki/Bundesliga")
    find_urls(html, base_url="https://en.wikipedia.org", output="Bundesliga")

    # Get urls from 2019-20_FIS_Alpine_Ski_World_Cup-page
    html = get_html("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
    find_urls(html, base_url="https://en.wikipedia.org", output="2019-20_FIS_Alpine_Ski_World_Cup")


# Tests to see if the find_articles-function works correctly
def test_find_articles():
    # Get articles from Nobel_Prize-page
    articles = find_articles("https://en.wikipedia.org/wiki/Nobel_Prize", "Nobel_Prize")

    # Get articles from Bundesliga-page
    articles = find_articles("https://en.wikipedia.org/wiki/Bundesliga", "Bundesliga")

    # Get urls from 2019-20_FIS_Alpine_Ski_World_Cup-page
    articles = find_articles("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup", "2019-20_FIS_Alpine_Ski_World_Cup")


#if __name__ == "__main__":
    #test_find_urls()
    #test_find_articles()
    