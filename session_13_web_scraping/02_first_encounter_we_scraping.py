import requests
from bs4 import BeautifulSoup

# Step 1: Request the Webpage
url = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved the webpage!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML Content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract the Titles of Articles
# On BBC News, titles might be inside <h3> or <h2> tags depending on the section
article_titles = soup.find_all(['h3', 'h2'], class_='gs-c-promo-heading__title')

# Step 4: Print the Titles
if article_titles:
    print("\nTop news headlines from BBC News:\n")
    for idx, title in enumerate(article_titles, start=1):
        print(f"{idx}. {title.get_text()}")
else:
    print("No titles found. The structure of the page might have changed.")

# Optional: Save the titles to a text file
with open('bbc_news_titles.txt', 'w') as file:
    for title in article_titles:
        file.write(title.get_text() + '\n')

if article_titles:
    print("\nTitles have been saved to 'bbc_news_titles.txt'")
else:
    print("\nNo titles to save.")
