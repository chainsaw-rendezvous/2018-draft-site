import csv
import os
from os import path
import shutil
import pathlib
import re
import glob

remove_previous_files = True
filename = "2023-carver-registration.csv"
image_url_prefix = 'https://register.chainsawrendezvous.org/wp-content/uploads/formidable/2/'
image_folder = './carver-photos-2023'
renamed_images = './carver-photos-2023-processed'

output_file = '2023-carvers.json'

try: 
    os.mkdir(image_folder) 
except OSError as error: 
    print(image_folder+" already exists.")

try: 
    os.mkdir(renamed_images) 
except OSError as error: 
    print(renamed_images+" already exists.")
    if remove_previous_files:
        print("Removing previously processed files")
        files = glob.glob(renamed_images+'/*', recursive=True)
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))
        print("\n")

approved = 0
fname = 1
lname = 2
state = 3
country = 4
website = 6
facebook = 8
twitter = 10
instagram = 9
youtube = 11
store = 7
image = 5

data = []
line = 0
output = "[\n"

with open(filename, 'r') as file:
    csvreader = csv.reader(file)

    fields = next(csvreader)

    for row in csvreader:
        new_row = ''
        new_row += "\t{\n"
        new_row += "\t\t\"name-last\": \"" + row[lname] + "\",\n"
        new_row += "\t\t\"name-first\": \"" + row[fname] + "\",\n"
        new_row += "\t\t\"name-nickname\": false,\n"
        new_row += "\t\t\"city\": false,\n"
        new_row += "\t\t\"state\": \"" + row[state] + "\",\n"
        new_row += "\t\t\"country\": \"" + row[country] + "\",\n"
        has_image = False
        if row[image]:
            img_path = image_folder + "/" + row[image].replace(image_url_prefix,'')
            print(img_path+" file expected")
            if path.exists(img_path):
                print(img_path+" file exists")
                file_extension = pathlib.Path(img_path).suffix
                new_name = (row[lname]+'-'+row[fname]).lower()
                new_name = re.sub(r'[^a-zA-Z0-9-]', '', new_name) + file_extension
                shutil.copy(img_path, renamed_images+"/"+new_name)
                print(img_path+" renamed to "+new_name+" and moved to proccessed folder")
                print("\n")
                row[image] = new_name
                has_image = True
            else:
                print(img_path+" file does NOT exist!!!!!!!!!!!!\n")
        
        if has_image:
            new_row += "\t\t\"image\": \"" + row[image] + "\",\n"
        else:
            new_row += "\t\t\"image\": false,\n"

        if row[facebook] or row[website] or row[twitter] or row[instagram] or row[youtube] or row[store]:
            new_row += "\t\t\"links\": {\n"
            needsBreak = 0
            if row[facebook]:
                if needsBreak:
                    new_row += "\t\t\t,\n"
                    needsBreak=0
                new_row += "\t\t\t\"Facebook\": {\n"
                new_row += "\t\t\t\"icon\": \"fab fa-facebook-f\",\n"
                new_row += "\t\t\t\"link\": \"" + row[facebook] + "\"\n"
                new_row += "\t\t\t}\n"
                needsBreak=1
            if row[website]:
                if needsBreak:
                    new_row += "\t\t\t,\n"
                    needsBreak=0
                new_row += "\t\t\t\"Website\": {\n"
                new_row += "\t\t\t\"icon\": \"fas fa-globe\",\n"
                new_row += "\t\t\t\"link\": \"" + row[website] + "\"\n"
                new_row += "\t\t\t}\n"
                needsBreak=1
            if row[instagram]:
                if needsBreak:
                    new_row += "\t\t\t,\n"
                    needsBreak=0
                new_row += "\t\t\t\"Instagram\": {\n"
                new_row += "\t\t\t\"icon\": \"fab fa-instagram\",\n"
                new_row += "\t\t\t\"link\": \"" + row[instagram] + "\"\n"
                new_row += "\t\t\t}\n"
                needsBreak=1
            if row[youtube]:
                if needsBreak:
                    new_row += "\t\t\t,\n"
                    needsBreak=0
                new_row += "\t\t\t\"YouTube\": {\n"
                new_row += "\t\t\t\"icon\": \"fab fa-youtube\",\n"
                new_row += "\t\t\t\"link\": \"" + row[youtube] + "\"\n"
                new_row += "\t\t\t}\n"
                needsBreak=1
            if row[store]:
                if needsBreak:
                    new_row += "\t\t\t,\n"
                    needsBreak=0
                new_row += "\t\t\t\"Store\": {\n"
                new_row += "\t\t\t\"icon\": \"fas fa-tags\",\n"
                new_row += "\t\t\t\"link\": \"" + row[store] + "\"\n"
                new_row += "\t\t\t}\n"
                needsBreak=1
            new_row += "\t\t}\n"
        else:
            new_row += "\t\t\"links\": false\n"
        new_row += "\t}"
        new_row += ",\n"
        output += new_row
        line += 1
output += "]"

output = re.sub(r',\s\]', '\n]', output)

#print(output)

print("Total no. of rows: %d"%(csvreader.line_num))

f = open("./"+output_file, "w")
f.write(output)
f.close()
