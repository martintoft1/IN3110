# Import necessary modules
from requesting_urls import get_html  
import re  # Regex
from bs4 import BeautifulSoup
import os  


def extract_events(url):
    """Extracts date, venue and discipline for competitions.

    The format of the data has to be equal to that of the Calendar in https://en.wikipedia.org/wiki/2021%E2%80%9322_FIS_Alpine_Ski_World_Cup#Calendar in order for the method to work.

    Args:
        url (str): The url to extract events from.
    Returns:
        table_info (list of lists): A nested list where the rows represent each race date, and the columns are [date, venue, discipline].
    """
    # Get the html
    html = get_html(url)

    # Make soup
    soup = BeautifulSoup(html, "html.parser")

    # Find the table contained in the Calendar
    calendar_header = soup.find(id="Calendar")
    calendar_table = calendar_header.find_all_next("table")[0]

    # Find the short- and full-names of the different disciplines in the table, and 
    # make a dictionary with the two-character short-form as key and the full name as value
    # Find string with the different disciplines
    discipline_caption = calendar_header.find_all_next("caption")[0]
    # Find keys 
    key_regex = r"[A-Z]{2}"
    discipline_keys = re.findall(key_regex, discipline_caption.get_text())
    # Find values
    discipline_tags = discipline_caption.find_all_next("a")
    discipline_values = []
    for tag in discipline_tags:
        discipline_values.append(tag.get_text())
    # Make dictionary
    disciplines = {}
    for i in range(len(discipline_keys)):
        disciplines[discipline_keys[i]] = discipline_values[i]

    # Find the rows in the table
    rows = calendar_table.find_all("tr")

    # Parse the row of 'th'-cells to identify the indices for Event, Venue, and Type (discipline)
    event_index = None
    venue_index = None 
    discipline_index = None 
    # Create list with all the header tags, knowing that the header-row is the first row in the table
    th_list = rows[0].find_all("th")
    # Indentify indices 
    i = 0
    for th in th_list:
        th = str(th)
        if "Event" in th:
            event_index = i 
        elif "Venue" in th:
            venue_index = i
        elif "Type" in th:
            discipline_index = i 
        i += 1

    # Set length for a "normal" full and short row
    # Full row means that it contains all the types of information listed 
    # in the header, making it the same length as the header-list
    full_row_length = len(th_list)
    # Short row means that the venue and slope is repeated from the last 
    # row(s), making it two shorter than the full row
    short_row_length = full_row_length - 2

    # List for saving all the events 
    events = []
    # String for saving last venue in case of repeated row
    last_venue = ""
    # Find events
    for row in rows:
        cells = row.find_all("td")

        # debug
        # TODO: Fjerne når dette virker
        #print(f"new row: {len(cells)} cells")
        #for idx, cell in enumerate(cells):
        #    print(f"  cell {idx}: {cell}")

        # Ignore rows with number of cells different from full and short row, as 
        # we have no means of knowing where the Date, Venue and Type cells are situated
        if len(cells) not in {full_row_length, short_row_length}:
            continue 

        
        # Get event-number
        event = cells[event_index].text.strip()

        # Get venue 
        if len(cells) == full_row_length:
            venue = cells[venue_index].text.strip()
            # Update last_venue 
            last_venue = venue
        else:  # Short row
            # Repeated venue, i.e same venue as last row
            venue = last_venue

        # Get full discipline name
        if len(cells) == full_row_length:
            discipline_short = cells[discipline_index].text.strip()
        else:  # Short row
            discipline_short = cells[discipline_index - 2].text.strip()
        # Strip short discipline name of suffix (reuse the regex-pattern from earlier)
        discipline_short = re.findall(key_regex, discipline_short)[0]
        # Find full name
        discipline = disciplines[discipline_short]

        # Add new event to events-list
        events.append((event, venue, discipline))

    return events


def create_betting_slip(events, save_as):
    """Saves a markdown format betting slip to the location ´./datetime_filter/<save_as>.md´.

    Args:
        events (list): A list of 3-tuples containing date, venue and type for each event.
        save_as (string): Filename to save the markdown betting slip as.
    """
    # Check if directory exists
    os.makedirs("datetime_filter", exist_ok=True)

    with open(f"./datetime_filter/{save_as}.md", "w") as out_file:
        out_file.write(f"# BETTING SLIP ({save_as})\n\nName:\n\n")
        out_file.write("Date | Venue | Discipline | Who wins?\n")
        out_file.write(" --- | --- | --- | --- \n")
        for e in events:
            date, venue, type = e 
            out_file.write(f"{date} | {venue} | {type} | \n")
