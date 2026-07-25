import requests
query = input("What type of news you interested in today?\n")
api = "8" #Enter your api key here from news api
url = "m"

print(url)

r = requests.get(url)

data = r.json()
articles =data["articles"]

for index,article in enumerate(articles):
    print(index+1,article["title"], article["url"])

    print("\n---------------------\n")


