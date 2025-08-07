import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://www.bbc.com/news"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h2.get_text().strip() for h2 in soup.find_all('h2') if h2.get_text().strip()]
    
    if not headlines:
        print("No headlines found. Check if the website structure has changed.")
    return headlines

def save_headlines(headlines, filename="headlines.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for i, headline in enumerate(headlines, 1):
                file.write(f"{i}. {headline}\n")
        print(f"Headlines saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def main():
    print("News Headline Scraper")
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)
    
    if headlines:
        save_headlines(headlines)
        print(f"Found {len(headlines)} headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
    else:
        print("Failed to retrieve headlines.")

if __name__ == "__main__":
    main()