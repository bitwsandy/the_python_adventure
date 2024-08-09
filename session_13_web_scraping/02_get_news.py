from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 2: Open the Website
url = 'https://www.bbc.com/news'
driver.get(url)

# Step 3: Extract the Titles
article_titles = driver.find_elements(By.CSS_SELECTOR, 'h3.gs-c-promo-heading__title')

# Step 4: Print the Titles
print("\nTop news headlines from BBC News:\n")
for idx, title in enumerate(article_titles, start=1):
    print(f"{idx}. {title.text}")

# Optional: Save the titles to a text file
with open('bbc_news_titles_selenium.txt', 'w') as file:
    for title in article_titles:
        file.write(title.text + '\n')

print("\nTitles have been saved to 'bbc_news_titles_selenium.txt'")

# Step 5: Close the WebDriver
driver.quit()
