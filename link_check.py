import requests
from bs4 import BeautifulSoup
from datetime import datetime
from argparse import ArgumentParser
from time import sleep


def main():
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-d", "--delay", help="seconds between reqeuests (int)",
                        action="store", type=int)
    args = parser.parse_args()

    # Uses the current date and time to add to the output filename so you
    # don't overwrite a previous output file if you execute the script twice
    now = datetime.now()
    date_time = now.strftime("%m%d%Y-%H%M%S")
    filename= 'url_check_results'+date_time+'.txt'

    # Validate sleep delay is integer between 0 and 60 seconds
    if args.delay:
        if int(args.delay) in range(0, 60, 1):
            print(args.delay , "second delay between requests")
        else:
            print("Argument Error.  Sleep delay must be an integer (1, 2, etc).")
            exit()

    # Read URLs from the 'urls.txt' file
    with open('urls.txt', 'r') as urls_file:
        urls = urls_file.read().splitlines()

    # Open a file to write the results
    with open(filename, 'w') as f:
        # Loop through each URL
        for url in urls:
            record = ""
            try:
                # Send a GET request to the URL
                response = requests.get(url)

                # Check the response status code
                if response.status_code == 200:
                    # Use BeautifulSoup to extract the title of the web page
                    soup = BeautifulSoup(response.content, 'html.parser')
                    title = soup.title.string
                    record = f"{url}\t{response.status_code}\t{title}"
                else:
                    # Write the URL and status code to the file
                    record = f"{url}\t{response.status_code}"
            except AttributeError as ae:
                # Handle 'NoneType' object error
                record = f"{url}\t{response.status_code}"
            except Exception as e:
                # Write the URL and error to the file
                record =f"{url}\t{str(e)}"
            # Write record to file
            f.write(record + "\n")

            # If verbose output selected, print each request result to screen
            if args.verbose:
                print(record)

            # If sleep delay selected, pause number of seconds before next request
            if args.delay:
                sleep(int(args.delay))


if __name__=="__main__":
    main()
