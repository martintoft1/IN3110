from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from webvisualization_plots import plot_reported_cases_per_million
from typing import Optional
from datetime import datetime

# Initialize app and templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount the static directories
app.mount(
    # The URL where these files will be available
    "/static",
    StaticFiles(
        # The directory the files are in
        directory="static/",
        html=True,
    ),
    # An internal name for FastAPI
    name="static",
)


@app.get("/")
def plot_reported_cases_per_million_html(request: Request):
    """
    Handle requests that go to the path "/", i.e. the root route for the web application.
    """
    return templates.TemplateResponse(
        "plot_reported_cases_per_million.html",
        {
            "request": request
        },
    )


@app.get("/plot_reported_cases_per_million.json")
def plot_reported_cases_per_million_json(countries: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None):
    """Return chart from altair as a dictionary so that it can be displayed on the web"""
    # Split countries into list
    if countries:
        countries = countries.split(",")

    # Make chart
    chart = plot_reported_cases_per_million(countries, start, end)

    # Return chart as dictionary
    return chart.to_dict()


def main():
    """Called when run as a script. Runs the app."""
    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    main()