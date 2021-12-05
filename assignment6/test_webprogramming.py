# Import modules to be tested
#from webvisualization_plots import get_data_from_csv
from webvisualization_plots import plot_reported_cases_per_million

def test_plot_reported_cases_per_million():
    """Tests the plot_reported_cases_per_million-function from webvisualization_plots"""
    # With no args
    chart = plot_reported_cases_per_million()
    # With country
    chart = plot_reported_cases_per_million(countries=["Argentina"])
    # With start-date 
    chart = plot_reported_cases_per_million(start="2020-05-01")
    # With end-date 
    chart = plot_reported_cases_per_million(end="2021-08-01")