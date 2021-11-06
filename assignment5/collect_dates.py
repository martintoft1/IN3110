# Import necessary modules
from requesting_urls import get_html  
import os  # For writing to file
import re  # Regex
from datetime import datetime  # For sorting


def find_dates(url, output=None):
    """
    Finds all dates in a html string.

    The returned list is in the following format:
    - 1999/01/13

    The following formats are considered when searching:
    DMY: 3 Aug(ust) 2020
    MDY: Aug(ust) 3, 2020
    YMD: 2020 Aug(ust) 3
    ISO: 2020-08-03

    Args:
        url (str): The webpage that the function is to scan for dates
        output (str): Name of the txt-file that the list of dates should be written to
    Returns:
        dates (list): A list with all the dates found in YYYY/MM/DD-fomat
    """
    # Create patterns for the day
    # Day-pattern for DMY, MDY and YMD, where day can be both one-digit and two-digit
    day = r"\b[0-3]?[0-9]\b"
    # Day-pattern for ISO where day has to be two-digit
    day_iso = r"\b[0-3][0-9]\b"

    # Create patterns for the month
    # Month-pattern for DMY, MDY and YMD, where the month is written as a word
    # Includes the abbreviated months
    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[fF]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM]ay\b"
    june = r"\b[jJ]une\b"
    july = r"\b[jJ]uly\b"
    aug = r"\b[aA]ug(?:ust)?\b"
    sept = r"\b[sS]ept(?:ember)?\b"
    oct = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"
    # Combine the patterns into one common pattern for the month
    month = rf"(?:{jan}|{feb}|{mar}|{apr}|{may}|{june}|{july}|{aug}|{sept}|{oct}|{nov}|{dec})" 
    # Month-pattern for ISO where month is written as a number, and has to be two-digit 
    month_iso = r"\b[0-1][0-9]\b"

    # Create pattern for the year (same for DMY, MDY, YMD and ISO)
    year = r"\b[0-2][0-9][0-9][0-9]"
    
    # Create patterns for the dates on the different date-formats
    dmy = rf"(?:{day} {month} {year})"
    mdy = rf"(?:{month} {day}, {year})"
    ymd = rf"(?:{year} {month} {day})"
    iso = rf"(?:{year}-{month_iso}-{day_iso})"

    # Get the html source-file string
    html_str = get_html(url)

    # Extract all the dates from the html string using the different date-formats
    dmy_dates = re.findall(dmy, html_str)
    mdy_dates = re.findall(mdy, html_str)
    ymd_dates = re.findall(ymd, html_str)
    iso_dates = re.findall(iso, html_str)

    # Convert the dates from the different date-formats to YYYY/MM/DD-fomat

    # dmy
    # Convert to y/m/d format
    dmy_len = len(dmy_dates)
    for i in range(dmy_len):
        dmy_dates[i] = re.sub(rf"({day})\s({month})\s({year})", r"\3/\2/\1", dmy_dates[i])
    # Make days double-digit if not already
    convert_days_to_double_digit(dmy_dates, year, month, day)
    # Change months to numbers
    convert_months_to_numbers(dmy_dates, year, month, day)

    # mdy
    # Convert to y/m/d format
    mdy_len = len(mdy_dates)
    for i in range(mdy_len):
        mdy_dates[i] = re.sub(rf"({month})\s({day}),\s({year})", r"\3/\1/\2", mdy_dates[i])
    # Make day double-digit if not already
    convert_days_to_double_digit(mdy_dates, year, month, day)
    # Change months to numbers
    convert_months_to_numbers(mdy_dates, year, month, day)
    
    # ymd
    # Convert to y/m/d format
    ymd_len = len(ymd_dates)
    for i in range(ymd_len):
        ymd_dates[i] = re.sub(rf"({year})\s({month})\s({day})", r"\1/\2/\3", ymd_dates[i])
    # Make day double-digit if not already
    convert_days_to_double_digit(ymd_dates, year, month, day)
    # Change months to numbers
    convert_months_to_numbers(ymd_dates, year, month, day)
    
    # iso
    # Convert to y/m/d format
    iso_len = len(iso_dates)
    for i in range(iso_len):
        iso_dates[i] = re.sub(rf"({year})-({month_iso})-({day_iso})", r"\1/\2/\3", iso_dates[i])
    
    # Merge all the lists of dates to one list
    dates = dmy_dates + mdy_dates + ymd_dates + iso_dates

    # Sort list of dates 
    dates.sort(key = lambda date: datetime.strptime(date, "%Y/%m/%d"))

    # Check if the output-argument was given; if so, write dates to
    # file with name "<output>_dates.txt" in the "collect_dates_regex"-directory 
    if output:
        # Create articles-string 
        dates_str = ""
        for date in dates:
            dates_str += date + "\n"

        # Write to file
        # Check if directory exists
        os.makedirs("collect_dates_regex", exist_ok=True)
        # Save current directory
        path = os.getcwd()
        # Switch to "collect_dates_regex"-directory and write to file
        os.chdir("collect_dates_regex")
        f = open(output + ".txt", "w")
        f.write(dates_str)
        f.close()
        # Change back to the current directory
        os.chdir(path)

    return dates


def convert_days_to_double_digit(dates, year, month, day):
    """
    Converts the days in each date in a list of dates to double-digit if they're not already double-digit

    Args:
        dates (list): List of dates
        year (pattern): Pattern for year
        month (pattern): Pattern for month
        day (pattern): Pattern for day
    """
    dates_len = len(dates)
    for i in range(dates_len):
        # Find day-string and -value
        day_month = re.findall(day, dates[i])[0]
        day_month_int = int(day_month)
        # Convert to double-digit based on day-value
        if day_month_int < 10:
            dates[i] = re.sub(rf"({year})/({month})/({day})", rf"\1/\2/0{day_month_int}", dates[i])


def convert_months_to_numbers(dates, year, month, day):
    """
    Converts the month in each date in a list of dates to a number

    Args:
        dates (list): List of dates
        year (pattern): Pattern for year
        month (pattern): Pattern for month
        day (pattern): Pattern for day
    """
    dates_len = len(dates)
    for i in range(dates_len):
        # Find month-string
        date_month = re.findall(month, dates[i])[0]
        # Convert to number based on month-string
        if date_month.lower().startswith("jan"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/01/\3", dates[i])
        elif date_month.lower().startswith("feb"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/02/\3", dates[i])
        elif date_month.lower().startswith("mar"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/03/\3", dates[i])
        elif date_month.lower().startswith("apr"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/04/\3", dates[i])
        elif date_month.lower().startswith("may"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/05/\3", dates[i])
        elif date_month.lower().startswith("june"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/06/\3", dates[i])
        elif date_month.lower().startswith("july"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/07/\3", dates[i])
        elif date_month.lower().startswith("aug"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/08/\3", dates[i])
        elif date_month.lower().startswith("sep"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/09/\3", dates[i])
        elif date_month.lower().startswith("oct"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/10/\3", dates[i])
        elif date_month.lower().startswith("nov"):
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/11/\3", dates[i])
        else:  # dec
            dates[i] = re.sub(rf"({year})/({month})/({day})", r"\1/12/\3", dates[i])
