import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Uses the current date and time to add to the output filename so you don't overwrite a previous output file if you execute the script twice
now = datetime.now()
date_time = now.strftime("%m%d%Y-%H%M%S")
filename= 'url_check_results'+date_time+'.txt'

# Read URLs from the 'urls.txt' file
with open('urls.txt', 'r') as urls_file:
    urls = urls_file.read().splitlines()

# Open a file to write the results
with open(filename, 'w') as f:
    # Loop through each URL
    for url in urls:
        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Check the response status code
            if response.status_code == 200:
                # Use BeautifulSoup to extract the title of the web page
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.string

                # Write the URL, status code, and title to the file
                f.write(f"{url}\t{response.status_code}\t{title}\n")
            else:
                # Write the URL and status code to the file
                f.write(f"{url}\t{response.status_code}\n")
        except AttributeError as ae:
            # Handle 'NoneType' object error
            f.write(f"{url}\t{response.status_code}\n")
        except Exception as e:
            # Write the URL and error to the file
            f.write(f"{url}\t{str(e)}\n")
