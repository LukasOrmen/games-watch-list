from sys import argv
from json import loads, dumps
from os import getcwd, getlogin
from pathlib import Path


if not len(argv) > 1:
    print("Requires at least 1 argument: python3 settings.py [argument] [true/false]")
    exit()

with open("settings.json", "r") as f:
    settings = loads(f.read())

if "-autostart" == argv[1]:
    if "true" == argv[2]:
        settings["settings"]["autostart"] = True
        with Path(f"C:\\Users\\{getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\gameswatchlist.bat").open("w") as f:
            f.write("python3 " + settings["path"])
        print("Autostart is now active.")
    else:
        settings["settings"]["autostart"] = False
        with Path(f"C:\\Users\\{getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\gameswatchlist.bat").open("w") as f:
            f.write("")
        print("Autostart is now deactive.")
elif "-alwaysshow" == argv[1]:
    if "true" == argv[2]:
        settings["settings"]["alwaysshow"] = True
        print("Always show is now active.")
    else:
        settings["settings"]["alwaysshow"] = False
        print("Always show is now deactive.")
elif argv[1] == "-steamid":
    print(argv[2] + ", is the new steam id linked to your account")
    if len(argv) > 2 and int(argv[2]):
        settings["steamid"] = argv[2] 
elif argv[1] == "-update-path":
    settings["path"] = getcwd() + "\\main.py"

with open("settings.json", "w") as f:
    f.write(dumps(settings))
