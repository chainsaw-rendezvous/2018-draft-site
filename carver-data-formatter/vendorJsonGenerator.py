import csv
import os
from os import path
import shutil
import pathlib
import re
import glob
import json
from operator import itemgetter, attrgetter
from collections import OrderedDict

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

remove_previous_files = True
filename = "2026-vendor-registration-2026-03-09.csv"
image_url_prefix = ''
image_folder = './vendor-photos-2026'
renamed_images = './vendor-photos-2026-processed'

output_file = '2026-vendors.json'
line = 0

regId = 0
paid = 1
organization = 3
type = 4
description = 15
website = 17
facebook = 18
instagram = 20
twitter = 19
threads = 21
youtube = 22
logo = 25
payment = 16

vendors = []

def isNotBlank(s):
    return bool(s and not s.isspace())

with open(filename, 'r') as file:
    csvreader = csv.reader(file)

    fields = next(csvreader)

    for row in csvreader:
        v = {}
        v["organization"] = row[organization]
        v["type"] = row[type]
        v["description"] = row[description]
        v["payment"] = row[payment]
        links = {}
        if isNotBlank(row[website]):
            links["url"] = {
                "icon": "fa-solid fa-globe",
                "link": row[website]
			}
            
        if isNotBlank(row[facebook]):
            links["facebook"] = {
                "icon": "fa-brands fa-facebook-f",
                "link": row[facebook]
			}
            
        if isNotBlank(row[instagram]):
            links["instagram"] = {
                "icon": "fa-brands fa-instagram",
                "link": row[instagram]
			}

        if isNotBlank(row[twitter]):
            links["twitter"] = {
                "icon": "fa-brands fa-x-twitter",
                "link": row[twitter]
			}

        if isNotBlank(row[threads]):
            links["threads"] = {
                "icon": "fa-brands fa-treads",
                "link": row[threads]
			}

        if isNotBlank(row[youtube]):
            links["youtube"] = {
                "icon": "fa-brands fa-youtube",
                "link": row[youtube]
			}

        if bool(links):
            v["links"] = links

        if isNotBlank(row[logo]):
            v["logo"] = row[logo]

        vendors.append(v)
        line += 1

# Sort vendors alphabetically
sorted_vendors = sorted(vendors, key=itemgetter('organization'))


# Convert Python to JSON  
json_object = json.dumps(sorted_vendors, indent = 4) 

# Print JSON object
print(json_object) 


f = open("./"+output_file, "w")
f.write(json_object)
f.close()