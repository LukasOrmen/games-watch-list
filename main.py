from datetime import datetime, date
from os import system
import requests
import json

system("cls")
#loading settings
with open("settings.json") as f:
    settings = json.loads(f.read())

#loading and parsing the API json
r = json.loads(requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?").text)
all_games = r["data"]["Catalog"]["searchStore"]["elements"]

titles = []

print("--- Free games in epic games store ---")
for game in all_games:
    title = game["title"]
    price = game["price"]["totalPrice"]["fmtPrice"]["discountPrice"]
    promotions = game["promotions"]


    if price == "0" and promotions != None: # Limted free games
        try:
            if title == "Mystery Game":
                pass
            else:
                print(title)
                titles.append(title)
                raw_enddate = game["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["endDate"]
                encoded_enddate = datetime.strptime(raw_enddate, '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%Y-%#m-%#d").split("-")
                final_encoded_date = date(int(encoded_enddate[0]), int(encoded_enddate[1]), int(encoded_enddate[2]))

                startdate = datetime.now().strftime("%Y-%#m-%#d").split("-")
                currentDate = date(int(startdate[0]), int(startdate[1]), int(startdate[2]))

                days_left = final_encoded_date - currentDate
                print(str(days_left).split(",")[0] + " left of the offer.\n")
        except IndexError:
            pass


#STEAM GAMES
steamid = settings["steamid"]
api_url = f"https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata"

games = {}

jdata = json.loads(requests.get(api_url).text)
for appid, gamedata in jdata.items():
    title = gamedata["name"]
    if gamedata["is_free_game"]:
        price = "Free"
    else:
        try:
            price = str(int(gamedata["subs"][0]["price"]) / 100)
        except IndexError:
            price = "Game not released"
    games[title] = price

print("\n--- Steam games ---")
for title_, price_ in games.items():
    print(title_.center(20) + price_.center(60))


if settings["settings"]["alwaysshow"] == True:
    input()
else:
    common = str(set(titles) & set(settings["games"]["epicgames"]))
    if common == "set()":
        input()
    elif not settings["games"]["steam"] == games:
        input()

with open("settings.json", "r") as f:
    data = json.loads(f.read())
for t in titles:
    if not t in settings["games"]["epicgames"]:
        data["games"]["epicgames"].append(t)
for title, price in games.items():
    data["games"]["steam"][title] = price
with open("settings.json", "w") as f:
    f.write(json.dumps(data))
