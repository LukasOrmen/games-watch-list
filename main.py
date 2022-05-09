from datetime import datetime
from datetime import date
import requests
import json

with open("settings.json", "r") as f:
    data = json.loads(f.read())


if not data["weeknum"] == int(datetime.today().strftime('%V')):
    r = json.loads(requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?").text)
    all_games = r["data"]["Catalog"]["searchStore"]["elements"]

    limited = []
    freegames = []

    for game in all_games:
        title = game["title"]
        price = game["price"]["totalPrice"]["fmtPrice"]["discountPrice"]
        original_price = game["price"]["totalPrice"]["originalPrice"]
        promotions = game["promotions"]

        if price == "0" and promotions != None:
            limited.append(title)
        elif price == "0":
            freegames.append(title)

    print("--- Limited Free Games ---")
    for games in limited:

        year = date.today().strftime("%Y")
        month = date.today().strftime("%m")
        day = date.today().strftime("%d")
        startDate = date(int(year), int(month), int(day))
        endDate = date(int(games["effectiveDate"].split("T")[0]))
        diff = startDate - endDate
        print(diff.days)

    print("\n\n--- Non Limited Free Games ---")
    for games in freegames:
        print(games)


#updating week number
    with open("settings.json", "r") as f:
        data = json.loads(f.read())
    data["weeknum"] = int(datetime.today().strftime('%V')) + 1
    with open("settings.json", "w") as f:
        f.write(json.dumps(data))
