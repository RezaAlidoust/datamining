import json
from pprint import pprint

from os import listdir

finance_path = "/Users/a/Documents/datamining/finance/selected"
political_path = "/Users/a/Documents/datamining/political/selected"
travel_path = "/Users/a/Documents/datamining/travel/selected"
technology_path = "/Users/a/Documents/datamining/technology/selected"

counter = 0
for file_name in listdir(finance_path):
    with open(finance_path + "/" + file_name) as json_file:
        data = json.load(json_file)
        text = data['text'].encode("utf-8")  # change encoding

        #  save file
        text_file = open("finance" + str(counter) + ".txt", "w")
        text_file.write(text)
        text_file.close()
        counter += 1
counter = 0
for file_name in listdir(political_path):
    with open(political_path + "/" + file_name) as json_file:
        data = json.load(json_file)
        text = data['text'].encode("utf-8")  # change encoding

        #  save file
        text_file = open("political" + str(counter) + ".txt", "w")
        text_file.write(text)
        text_file.close()
        counter += 1
counter = 0
for file_name in listdir(travel_path):
    with open(travel_path + "/" + file_name) as json_file:
        data = json.load(json_file)
        text = data['text'].encode("utf-8")  # change encoding

        #  save file
        text_file = open("travel" + str(counter) + ".txt", "w")
        text_file.write(text)
        text_file.close()
        counter += 1
counter = 0
for file_name in listdir(technology_path):
    with open(technology_path + "/" + file_name) as json_file:
        data = json.load(json_file)
        text = data['text'].encode("utf-8")  # change encoding

        #  save file
        text_file = open("technology" + str(counter) + ".txt", "w")
        text_file.write(text)
        text_file.close()
        counter += 1
