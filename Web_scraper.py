import requests
from bs4 import BeautifulSoup


URL = "https://www.bbc.com/news"
response = requests.get(URL)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


    headlines = []
    for tag in soup.find_all('h2'):
        text = tag.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    with open("headlines.txt", "w", encoding='utf-8') as file:
        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")

    print(f"✅ {len(headlines)} headlines saved to headlines.txt")
else:
    print(f"❌ Failed to retrieve page. Status code: {response.status_code}")
