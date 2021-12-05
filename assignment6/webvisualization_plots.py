#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import altair as alt
import pandas as pd


def get_data_from_csv(columns, countries=None, start=None, end=None):
    """Creates pandas dataframe from a .csv-file.

    Data will be filtered based on data column name, list of countries to be plotted and
    time frame chosen.

    Args:
        columns (list(string)): a list of data columns you want to include
        countries ((list(string), optional): List of countries you want to include.
            If none is passed, dataframe should be filtered for the 6 countries with the highest
            number of cases per million at the last current date available in the timeframe chosen.
        start (string, optional): The first date to include in the returned dataframe.
            If specified, records earlier than this will be excluded.
            Default: include earliest date
            Example format: "2021-10-10"
        end (string, optional): The latest date to include in the returned data frame.
            If specified, records later than this will be excluded.
            Example format: "2021-10-10"
    Returns:
        cases_df (dataframe): dataframe for the timeframe, columns, and countries chosen
    """
    # Path to .csv file containing covid-data
    path = "owid-covid-data.csv"

    # Read given columns from .csv file, and parse dates
    df = pd.read_csv(
        path,
        sep=",",
        usecols=["location"] + ["date"] + columns,
        parse_dates=["date"],
        date_parser=lambda col: pd.to_datetime(col, format="%Y-%m-%d"),
    )

    # Set start-date
    if start:
        start_date = datetime.strptime(start, "%Y-%m-%d")
    else:
        # No start date specified, pick first date available
        start_date = df.date.iloc[0]

    # Set end-date
    if end:
        end_date = datetime.strptime(end, "%Y-%m-%d")
    else:
        # No end date specified, pick latest date available
        end_date = df.date.iloc[-1]

    # Check if start-date is earlier than end-date
    if start_date >= end_date:
        raise ValueError("The start date must be earlier than the end date.")

    # Check if countries is specified
    if not countries:
        # No countries specified, pick 6 countries with the highest case count at end date
        # Get rows based on end date
        df_latest_dates = df[df.date.isin([end_date])]
        # Get a list with the names of the 6 countries with the highest case count on end date
        countries = df_latest_dates.dropna(subset=["new_cases_per_million"]).sort_values("new_cases_per_million").tail(6)["location"].tolist()

    # Filter to include only the data from the selected countries in the dataframe
    cases_df = df[df["location"] == countries[0]]
    for i in range(1, len(countries)):
        cases_df = cases_df.append(df[df["location"] == countries[i]])
   
    # Exclude records earlier than start_date and later than end date 
    cases_df = cases_df[cases_df["date"] >= start_date] 
    cases_df = cases_df[cases_df["date"] <= end_date] 

    return cases_df


def plot_reported_cases_per_million(countries=None, start=None, end=None):
    """Plots data of reported covid-19 cases per million.

    Args:
        countries ((list(string), optional): List of countries you want to filter.
            If none is passed, dataframe will be filtered for the 6 countries with the highest
            number of cases per million at the last current date available in the timeframe chosen.
        start (string, optional): a string of the start date of the table. 
            None of the dates will be older then this.
        end (string, optional): a string of the en date of the table
            None of the dates will be newer then this
    Returns:
        altair Chart of number of reported covid-19 cases over time.
    """
    # Set new_cases_per_million as one ofte the data columns to be extracted
    columns = ["new_cases_per_million"]

    # Create dataframe
    cases_df = get_data_from_csv(columns, countries, start, end)

    # Note: if you want to plot all countries simultaneously while enabling checkboxes, 
    # you might need to disable altairs max row limit by commenting in the following line
    # alt.data_transformers.disable_max_rows()

    # Create the chart
    chart = (
        alt.Chart(cases_df, title="Daily new confirmed covid-19 cases per million people")
        .mark_line()
        .encode(
            x=alt.X(
                "date:T",
                axis=alt.Axis(
                    format="%b, %Y", title="Date", titleFontSize=14, tickCount=20
                ),
            ),
            y=alt.Y(
                "new_cases_per_million",
                axis=alt.Axis(
                    title="Number of Reported Cases per Million",
                    titleFontSize=14,
                    tickCount=10,
                ),
            ),
            color=alt.Color("location:N", legend=alt.Legend(title="Country")),
        )
        .interactive()
    )
    return chart


def get_countries():
    """Returns unique country-names"""
    # Path to .csv file containing covid-data
    path = "owid-covid-data.csv"

    # Read given columns from .csv file, and parse dates
    df = pd.read_csv(
        path,
        sep=",",
        usecols=["location"]
    )

    return df.location.unique()


def main():
    """Function called when the file is run as a script

    Takes user-input, uses it to creates a chart, and displays the chart
    """
    # Take user-input
    print("\nGive input for arguments to the chart over recorded covid cases per million. If there is an argument you don't want to specify, press enter without writing anything to continue")

    # Get countries
    countries = input("\nEnter the countries you want to display (if no countries are specified, the countries with the most covid-cases at the end-date will be chosen): ")

    # Get start-date
    while True:
        start = input("\nEnter the start-date on the format YYYY-MM-DD (if no start-date is specified, the earliest date we have data from will be chosen): ")
        # Check if start-date was on correct format
        if start:
            try:
                datetime.strptime(start, "%Y-%m-%d")
                break
            except:
                # Wrong format
                print("The date was not written on the correct format.")
        else:
            break

    # Get end-date
    while True:
        end = input("\nEnter the end-date on the format YYYY-MM-DD (if no end-date is specified, the earliest date we have data from will be chosen): ")
        # Check if end-date was on correct format
        if end:
            try:
                datetime.strptime(end, "%Y-%m-%d")
                break
            except:
                # Wrong format
                print("The date was not written on the correct format.")
        else:
            break

    # Make the chart based on the user-input
    chart = plot_reported_cases_per_million(countries=countries, start=start, end=end)

    # Show the chart
    chart.show()


if __name__ == "__main__":
    main()
