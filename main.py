# Imports
from inlabs_auto_download_xml import login
import zipfile
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import pandas as pd

# Downloading Files
login()

# Extracting Files

folder_dir = Path('__file_').resolve().parent if "_file_" in locals() else Path.cwd()
        # __file = path of this file; .resolve = absolut path;
        # .parent = path of the parent folder
        # if "_file_" in locals() else Path.cwd() --- so it will work on Jupyter Notebooks

for f in os.listdir():  # lists everything in your current directory(default)
    if f[-3:] == 'zip':
        f_name = f
        break

file_path = folder_dir/f_name

with zipfile.ZipFile(file_path, 'r') as zipped:  # Extracting
    zipped.extractall(folder_dir/'extracted')

print('File Extracted')

# Looping Thru Extracted Folder, Parsing the .xml File and Retrieving Information

for xml_file in os.listdir(folder_dir/'extracted'):

    tree = ET.parse(folder_dir/'extracted'/xml_file)  # Parsing the XML file
    root = tree.getroot()  # Creating the root object

    for i, value in enumerate(root):
        article_data = value.attrib  # this xml has only one child with the article tag and a dictionary as an attribute

    text = root[0][0][5].text

# Reading the Excel File and Writing on It

names = pd.read_excel('servidores.xlsx')


# Delete zip file and the extract folder at the end
