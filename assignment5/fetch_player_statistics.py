# Import necessary modules
from requesting_urls import get_html  
import re  # Regex
from bs4 import BeautifulSoup
import os  
import matplotlib.pyplot as plt


# 1. Get the list of teams
# 2. Given a team url, get the list of players
# 3. Given a player url, get their statistics


def extract_team_urls(url):
    """Extracts the team-names and -urls from a NBA Playoff 'Bracket section table for the teams that made it to the conference semifinals.

    Args:
        url (str): The url for the wikipedia-page containing the bracket.
    Returns:
        team_names (list): A list containing the team names.
        team_urls (list): A list containing Wikipedia-urls corresponding to team_names.
    """
    # Base url
    base_url = "https://en.wikipedia.org"
    
    # Get html
    html_str = get_html(url)

    # Create soup
    soup = BeautifulSoup(html_str, "html.parser")

    # Find bracket and its content
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")

    # Find team teams
    # Find all the team names in the bracket
    team_list = []
    for i in range(2, len(rows)):
        # Get list of text contained in cells
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]
        # Filter out the cells that are empty
        cells_text = [cell for cell in cells_text if cell]
        # Find the cells that contain seeding, team name and games won, and extract team name
        if len(cells_text) == 3:
            team_list.append(cells_text[1])
    # Filter out the teams that appear more than once, which means they made it
    # to the conference semifinals
    team_names = []
    for team_name in team_list:
        if team_name not in team_names:
            if team_list.count(team_name) > 1:
                team_names.append(team_name)

    # Find urls to the team webpages
    team_urls = []
    for team_name in team_names:
        # Bool for breaking out of loops early
        found_url = False
        # Regex for matching the teams url
        url_regex = rf'(?<=href=")[^"]+(?=".+{team_name})'
        # Find url
        for i in range(2, len(rows)): 
            if found_url:
                break
            # Get list of cells
            cells = rows[i].find_all("td")
            # Get url
            for cell in cells:
                url = re.findall(url_regex, str(cell))
                if len(url) == 1:
                    # Add absolute url to team_urls
                    team_urls.append(base_url + url[0])
                    found_url = True

    return team_names, team_urls


def extract_players(team_url):
    """Extracts all the player names and urls from an NBA team's Wikipedia-page.

    Args:
        team_url (str): The url for the team's wikipedia-page.
    Returns:
        player_names (list): A list containing the player names
        player_urls (list): A list containing Wikipedia-urls corresponding to player_names.
    """
    # Base url
    base_url = "https://en.wikipedia.org"

    # Get html 
    html = get_html(team_url)

    # Make soup
    soup = BeautifulSoup(html, "html.parser")

    # Find Roster and its content
    roster_header = soup.find(id="Roster")
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # Find player names and urls
    player_names = []
    player_urls = []
    for i in range(1, len(rows)):  
        # Get list of text contained in cells
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]
        # Only interested in rows with 7 cells
        if len(cells_text) == 7:  
            # Find name
            player_names.append(cells[2].get_text(strip=True))
            # Find url
            rel_url = cells[2].find_next("a").attrs["href"]
            # Use regex to remove information in parenthesis following the name
            rel_url = re.findall(r'[^(]+', rel_url)[0]
            # Add absolute url to player_urls
            player_urls.append(base_url + rel_url)

    return player_names, player_urls
    

def extract_player_statistics(player_url):
    """Extracts the statistics of an NBA player. 

    Args:
        player_url (str): The url for the NBA player's Wikipedia-page.
    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.
    """
    # Set default score in case incomplete statistics
    ppg = 0.0
    bpg = 0.0
    rpg = 0.0

    # Get html
    html = get_html(player_url)

    # Make soup
    soup = BeautifulSoup(html, "html.parser")

    # Find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")
    # Check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")

    # Find regular season header and the table contained in it
    try:
        regular_season_header = nba_header.find_next(id="Regular_season")
        nba_table = regular_season_header.find_next("table")
    except:
        try:
            # Table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")
        except:
            # Return default score
            return ppg, bpg, rpg

    # Find nba table header and table rows
    table_header = nba_table.find_all("th")
    rows = nba_table.find_all("tr")

    # Find the columns for the different categories
    for i in range(len(table_header)):
        if "ppg" in table_header[i].get_text().lower():
            ppg_column = i
        elif "bpg" in table_header[i].get_text().lower():
            bpg_column = i
        elif "rpg" in table_header[i].get_text().lower():
            rpg_column = i

    # Extract the scores from the different categories
    # Find the row for the 2020-21 year, which is the second last column, only followed by "Career"
    row = rows[len(rows)-2]
    cells = row.find_all("td")
    # Set scores
    try:
        ppg = cells[ppg_column].get_text(strip=True)
    except:
        ppg = 0.0
    try:
        bpg = cells[bpg_column].get_text(strip=True)
    except:
        bpg = 0.0
    try:
        rpg = cells[rpg_column].get_text(strip=True)
    except:
        rpg = 0.0

    # Convert the scores extracted to floats
    # If the scores cannot be converted, set them to zero
    try:
        ppg = float(ppg)
    except ValueError:
        ppg = 0.0
    try:
        bpg = float(bpg)
    except ValueError:
        bpg = 0.0
    try:
        rpg = float(rpg)
    except ValueError:
        rpg = 0.0

    return ppg, bpg, rpg


def plot_NBA_player_statistics(teams, statistic):
    """Plots NBA player statistics.
    
    Args:
        teams (dict): A dictionary containing lists with tuples of NBA player statistics, where the key to each dictionary is the players' team. The tuples furthermore contain the attributes "name" which is the player's name, and "ppg" which is the player's average score per game.
        statistic (str): ppg, bpg or rpg
    """

    count_so_far = 0
    all_names = []

    # 8 different colors to choose from since we have 8 teams
    colors = ["b", "g", "r", "c", "m", "y", "k", "w"]

    # Choose plot-colors for each team
    color_table = []
    i = 0
    for team, players in teams.items():
        color_table.append({team: colors[i]})
        i += 1

    # Iterate through each team 
    i = 0
    for team, players in teams.items():
        # Pick the color for the team
        color = color_table[i][team]
        
        # Collect the statistic and name of each player on the team
        names = []
        statistics = []
        for player in players:
            for key, val in player.items():
                names.append(key)
                statistics.append(val)

        # Record all the names, for use later in x label
        all_names.extend(names)

        # The position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)

        # Make bars for this team's players ppg, bpg and rpg, with
        # the team name as the label, and the value as text on the bars
        # Ppg
        bars = plt.bar(x, statistic, color=color, label=team)
        plt.bar_label(bars)

        i += 1

    # Make the plots
    # Use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # Add the legend with the colors  for each team
    plt.legend(loc=0)
    # Turn off gridlines
    plt.grid(False)
    # Set the title
    if statistic == "ppg":
        plt.title("points per game")
    elif statistic == "bpg":
        plt.title("blocks per game")
    elif statistic == "rpg":
        plt.title("rebounds per game")
    # Save figure to file
    plt.savefig(f"{statistic}.png")


def find_top_three_each_team(url):
    """Finds the top three players for each team in the NBA Playoff 2020-2021 that made it to the conference semifinals based on different statistics.
    
    Makes three plots with the top players in the teams - one for each statistic. 

    Args:
        url (str): The url for the wikipedia-page containing the bracket with the teams.
    """
    # Get team names and urls
    team_names, team_urls = extract_team_urls(url)

    # Make team-dictionary with team names as keys and player lists with 
    # top 3 players as values 
    teams_ppg = {}
    teams_bpg = {}
    teams_rpg = {}

    # Get all the teams' player names and urls, and put them in list with same 
    # indices as the team they belong to
    team_player_names = []
    team_player_urls = []
    for i in range(len(team_urls)):
        player_names, player_urls = extract_players(team_urls[i])
        team_player_names.append(player_names)
        team_player_urls.append(player_urls)

    # Find the top three players from each team for each statistic, and
    # add them to the teams-dictionary
    for i in range(len(team_player_urls)):
        top_three_ppg = []
        top_three_bpg = []
        top_three_rpg = []
        # Find top 3 ppg for team
        for j in range(len(team_player_urls[i])):
            ppg, bpg, rpg = extract_player_statistics(team_player_urls[i][j])
            player_name = team_player_names[i][j]

            if len(top_three_ppg) < 3:
                top_three_ppg.append({player_name: ppg})
                top_three_bpg.append({player_name: bpg})
                top_three_rpg.append({player_name: rpg})

            else:
                for k in range(3):
                    for other_player_name, other_ppg in top_three_ppg[k].items():
                        if ppg > other_ppg:
                            top_three_ppg[k] = {player_name: ppg}

                for k in range(3):
                    for other_player_name, other_bpg in top_three_bpg[k].items():
                        if ppg > other_bpg:
                            top_three_bpg[k] = {player_name: bpg}

                for k in range(3):
                    for other_player_name, other_rpg in top_three_rpg[k].items():
                        if ppg > other_rpg:
                            top_three_rpg[k] = {player_name: rpg}
                        
            
            teams_ppg[team_names[i]] = top_three_ppg
            teams_bpg[team_names[i]] = top_three_bpg
            teams_rpg[team_names[i]] = top_three_rpg
                    

    # Plot the stats
    plot_NBA_player_statistics(teams_ppg, "ppg")
    plot_NBA_player_statistics(teams_bpg, "bpg")
    plot_NBA_player_statistics(teams_rpg, "rpg")

    # Return the dictionaries
    return teams_ppg, teams_bpg, teams_rpg


# Tests the find_top_three_each_team()-function
def test_find_top_three_each_team():
    url = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    find_top_three_each_team(url)


if __name__ == "__main__":
    test_find_top_three_each_team()