
import json

with open('settings.json', 'r') as confFile:
    config_debugFileSettings = json.load(confFile)
    print(config_debugFileSettings["projectSettings"])
