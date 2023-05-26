# urlcheck
URL check tool

This URL check tool is written to check the server response of links that are fed to the script in a file called 'urls.txt' placed in the same folder as the script, containing one url per line.
The output file 'url_check_results.txt' contains the url, the server response code and the page title.
If the script runs into an error, which is also a sign that the link is not working, the script notes the error response after the url in the output file.

## Usage

* In project directory, install requirements `pip install -r requirements.txt`
* Ensure that urls.txt exists in project directory
* Run application `python link_check.py`
* Review results file url_check_results...txt

### Options

feature-sleep
```
$ python link_check.py -h
usage: link_check.py [-h] [-v] [-d DELAY]

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -d DELAY, --delay DELAY

```
Verbose option prints results to stdout
```
$ python link_check.py -v
https://www.google.com/ 200     Google
https://www.bing.com/   200     Bing
https://example.com/    200     Example Domain
https://www.cnn.com/aewsre      404

```

Delay adds a delay between requests to avoid triggering download restrictions popular with
electronic resource providers.  Delay must be an integer between 0 and 60.

```
$ python link_check.py -v -d 2
2 second delay between requests
https://www.google.com/ 200     Google
https://www.bing.com/   200     Bing
https://example.com/    200     Example Domain
https://www.cnn.com/aewsre      404
```

Verbose option prints results to stdout

```
$ python link_check.py -h
usage: link_check.py [-h] [-v]

options:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity
```
