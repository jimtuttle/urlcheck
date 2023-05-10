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
