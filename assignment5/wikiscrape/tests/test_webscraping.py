# Import modules to be tested
import wikiscrape.requesting_urls as requesting_urls
import wikiscrape.collect_dates as collect_dates
import wikiscrape.filter_urls as filter_urls
import wikiscrape.time_planner as time_planner 
import wikiscrape.fetch_player_statistics as fetch_player_statistics 


def test_get_html():
    """Tests the get_html-function from requesting_urls"""
    # Check Studio_Ghibli-page
    # Without output
    html_str = requesting_urls.get_html("https://en.wikipedia.org/wiki/Studio_Ghibli")
    # With output
    html_str = requesting_urls.get_html("https://en.wikipedia.org/wiki/Studio_Ghibli", output="Studio_Ghibli")

    # Check Star_Wars-page
    # Without output
    html_str = requesting_urls.get_html("https://en.wikipedia.org/wiki/Star_Wars")
    # With output
    html_str = requesting_urls.get_html("https://en.wikipedia.org/wiki/Star_Wars", output="Star_Wars")

    # Check index-page with parameters
    # With one parameter
    html_str = requesting_urls.get_html("https://en.wikipedia.org/w/index.php", params={"title": "Main_Page"})
    # With two parameters and output
    html_str = requesting_urls.get_html("https://en.wikipedia.org/w/index.php", params={"title": "Main_Page", "action": "info"}, output="index")


def test_find_dates():
    """Tests the find_dates-function from collect_dates"""
    # Get dates from J._K._Rowling-page and write to file
    dates = collect_dates.find_dates("https://en.wikipedia.org/wiki/J._K._Rowling", "J._K._Rowling")

    # Get dates from Richard_Feynman-page and write to file
    dates = collect_dates.find_dates("https://en.wikipedia.org/wiki/Richard_Feynman", "Richard_Feynman")

    # Get dates from Hans_Rosling-page and write to file
    dates = collect_dates.find_dates("https://en.wikipedia.org/wiki/Hans_Rosling", "Hans_Rosling")


def test_find_urls():
    """Tests the find_urls-function from filter_urls"""
    # Get urls from Nobel_Prize-page
    html = requesting_urls.get_html("https://en.wikipedia.org/wiki/Nobel_Prize")
    filter_urls.find_urls(html, base_url="https://en.wikipedia.org", output="Nobel_Prize")

    # Get urls from Bundesliga-page
    html = requesting_urls.get_html("https://en.wikipedia.org/wiki/Bundesliga")
    filter_urls.find_urls(html, base_url="https://en.wikipedia.org", output="Bundesliga")

    # Get urls from 2019-20_FIS_Alpine_Ski_World_Cup-page
    html = requesting_urls.get_html("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup")
    filter_urls.find_urls(html, base_url="https://en.wikipedia.org", output="2019-20_FIS_Alpine_Ski_World_Cup")


def test_find_articles():
    """Tests the find_articles-function from filter_urls"""
    # Get articles from Nobel_Prize-page
    articles = filter_urls.find_articles("https://en.wikipedia.org/wiki/Nobel_Prize", "Nobel_Prize")

    # Get articles from Bundesliga-page
    articles = filter_urls.find_articles("https://en.wikipedia.org/wiki/Bundesliga", "Bundesliga")

    # Get urls from 2019-20_FIS_Alpine_Ski_World_Cup-page
    articles = filter_urls.find_articles("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup", "2019-20_FIS_Alpine_Ski_World_Cup")


def test_time_planner():
    """Tests the extract_events-function and the creating_betting_slip-method from time_planner"""
    # Get events from FIS_Alpine_Ski_World_Cup 2021-22 wikipedia-page
    events = time_planner.extract_events("https://en.wikipedia.org/wiki/2021%E2%80%9322_FIS_Alpine_Ski_World_Cup#Calendar")

    # Create betting slip from events"
    time_planner.create_betting_slip(events, "betting_slip_empty")


def test_find_top_three_each_team():
    """Tests the find_top_three_each_team()-function from fetch_player_statistics"""
    # Get top three for each team that made it to the conference semifinal in 
    # the 2021 NBA playoffs from the 2021_NBA_playoffs wikipedia-page
    teams_ppg, teams_bpg, teams_rpg = fetch_player_statistics.find_top_three_each_team("https://en.wikipedia.org/wiki/2021_NBA_playoffs")