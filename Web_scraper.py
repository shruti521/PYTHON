import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML content
URL = "https://www.bbc.com/news"
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Parse <h2> tags containing headlines
    headlines = []
    for tag in soup.find_all('h2'):
        text = tag.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    # Step 3: Save headlines to a text file
    with open("headlines.txt", "w", encoding='utf-8') as file:
        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")

    print(f"✅ {len(headlines)} headlines saved to headlines.txt")
else:
    print(f"❌ Failed to retrieve page. Status code: {response.status_code}")
