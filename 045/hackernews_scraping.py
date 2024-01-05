from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(
    selector=".titleline > a"
)  # ">" is the child combinator, which selects direct children of the preceding element.

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

print(article_texts)
print(article_links)
print(article_upvotes)
# for tag in article_tag:
#     print(tag.text)

highest_upvote = max(article_upvotes)
print(highest_upvote)
highest_upvote_index = article_upvotes.index(highest_upvote)
print(highest_upvote_index)
print(
    f"title: {article_texts[highest_upvote_index]} \nlink: {article_links[highest_upvote_index]}"
)
