News Headline Scraper

Overview

This is a Python command-line script that scrapes top news headlines from a website (default: BBC News) using requests and BeautifulSoup. It extracts headlines from <h2> tags and saves them to a text file (headlines.txt).

Features

Fetches headlines from a specified news website.
Saves headlines to headlines.txt with numbered entries.
Displays headlines in the console.
Includes error handling for network issues and file operations.

Requirements

Python 3.x

Libraries: requests, beautifulsoup4Install with:
pip install requests beautifulsoup4

How to Run

Save the script as scraper.py.
Run in a terminal:
python scraper.py
The script fetches headlines from https://www.bbc.com/news and saves them to headlines.txt.

Example Output (headlines.txt)

1. Breaking: Major Event Unfolds
2. Global Leaders Meet to Discuss Climate
...

Notes

Uses a user-agent to avoid being blocked.
Targets <h2> tags; adjust for other websites if needed.
Check the website’s terms of service and robots.txt before scraping.
