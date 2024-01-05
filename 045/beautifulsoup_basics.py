from bs4 import BeautifulSoup

with open("045\website.html", encoding="utf8") as file:
    content = file.read()
    # print(content)

soup = BeautifulSoup(content, "html.parser")

# print(soup.title) # returns the content wrapped inside the title tag including the title tag itself
# print(soup.title.name)  # returns the name of the tag
# print(soup.title.string)  # returns the content that is inside the title tag

# print(soup.prettify())  # returns the soup HTML code in an indented format

# print(soup.a) # returns the first anchor tag

all_anchor_tags = soup.find_all(
    name="a"
)  # retruns all the tags that matches the one given in the "name" parameter


# for tag in all_anchor_tags:
# print(tag.getText()) # returns the texts only from the tags
# print(tag.get("href"))  # returns the value of an attribute of the tag


# heading = soup.find(
#     name="h1", id="name"
# )  # returns the first element (since 'find()' method is used, use 'find_all()' method to find all the instances that have the same tag and attrtibutes) with h1 tag and id attribute set to "name"
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)


# using css selectors

# 'select_one()' returns the first item it finds
# 'select()' returns the list of items that have the corresponding selector

company_url = soup.select_one(
    selector="p a"
)  # returns the first matching item (<a> tag that is inside the <p> tag)
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)