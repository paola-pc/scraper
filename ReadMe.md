# Scraper

Scraper is a Python script for basic web scraping.

0. You need to have Python3 installed on your computer to run this program. 

1. Install dependencies: Beautiful Soup.
    - Install packages automatically by running `pip install -r requirements.txt` from the root folder on your CLI.
    - Alternatively, manually install version 4.12.2 of Beautiful Soup with the command `pip install beautifulsoup4==4.12.2`

**Note:** You can do this globally to run the script, or you can create a virtual enviroment for the project using `venv` and run it from within. The second approach is usually recommended as it won't interfere with or cause dependency conflicts with any other projects you run on your machine. 

2. From the root folder, run the main.py file on your CLI: `python3 main.py`. This will create a json file called 'data.json' containing the retrieved data.

3. You can run `cat data.json` to visualize the file.
