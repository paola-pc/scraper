# Scraper

Scraper is a Python script for basic web scraping.

0. You will need to have Python3 installed in your computer in order to run this program. 

1. Install dependencies: Beautiful soup.
- Install packages automatically running `pip install -r requirements.txt` in your command line.
- Or, install manually the 4.12.2 version of Beautiful soup `pip install beautifulsoup4==4.12.2`

**Note:** You can do this globally to run the app or, as an alternative, you can create a virtual enviroment for the project using `venv`. The second approach is usually recommended as it won't interfere or cause dependency conflicts with any other projects you run in your machine.

2. From the root folder, run the scraper.py on your CLI: `python3 scraper.py`. This will create a json file containing the data retrieved.

3. You can run `cat contact_results.json` to visualize this file.