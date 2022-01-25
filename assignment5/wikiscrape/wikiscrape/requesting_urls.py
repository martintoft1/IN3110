# Import necessary modules
import requests as req
import os


def get_html(url, params=None, output=None):
    """
    Gets and returns a html source-file string from an url.

    If the params-argument is given, the function gets and returns the data of the specified type. If the output-argument is given, the function prints the response-text and url to a txt-file with the name in the output-argument.

    Args:
        url (str): The url of the webpage that the function gets the html string from
        params (dict): Dictionary containing the parameters that are to be used when getting the html-reponse
        output (str): Name of the txt-file that the html string should be written to

    Returns:
        html_str (str): The string containing the source-file
    """
    # Execute the get-request
    response = req.get(url, params=params)

    # Check if get-request was succesful 
    assert response.status_code == 200

    # Get html-text
    html_str = response.text

    # Check if the output-argument was given
    if output:  # Write to file with name "ouput.txt" in the "requesting_urls"-directory
        # Check if directory exists
        os.makedirs("requesting_urls", exist_ok=True)
        # Save current directory
        path = os.getcwd()
        # Switch to "requesting_urls"-directory and write to file
        os.chdir("requesting_urls")
        f = open(output + ".txt", "w")
        f.write(html_str)
        f.close()
        # Change back to the current directory
        os.chdir(path)

    # Return reponse-text
    return html_str
