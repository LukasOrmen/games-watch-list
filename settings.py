from sys import argv
from json import loads, dumps


if not len(argv) > 2:
    print("Requires at least 2 arguments: python3 settings.py [argument] [true/false]")
    exit()

with open("settings.json", "r") as f:
    settings = loads(f.read())

if "-autostart" == argv[1]:
    if "true" == argv[2]:
        settings["settings"]["autostart"] = True
        print("Autostart is now active.")
    else:
        settings["settings"]["autostart"] = False
        print("Autostart is now deactive.")
elif "-alwaysshow" == argv[1]:
    if "true" == argv[2]:
        settings["settings"]["alwaysshow"] = True
        print("Always show is now active.")
    else:
        settings["settings"]["alwaysshow"] = False
        print("Always show is now deactive.")

with open("settings.json", "w") as f:
    f.write(dumps(settings))
