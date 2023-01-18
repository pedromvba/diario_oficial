# Imports
from inlabs_auto_download_xml import login
import zipfile
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import pandas as pd


# Defining Functions:

def listdir_nohidden(path):
    '''
    List only the "real" files (non system files from a path/directory)
    :param path: directory absolute path
    :return: iterable with the non system files from a path
    '''
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


# Downloading Files
login()

# Extracting Files

directory = 'extracted'
parent_dir = Path('__file_').resolve().parent if "_file_" in locals() else Path.cwd()
                                                        # __file = path of this file; .resolve = absolut path;
                                                        # .parent = path of the parent folder
                                                        # if "_file_" in locals() else Path.cwd() --- so it will work on Jupyter Notebooks
path = os.path.join(parent_dir, directory)
os.mkdir(path)  # Creating the folder where the extracted files will be added

for zipped_file in os.listdir():

    if zipped_file.endswith('.zip'):
        file_path = f'{parent_dir}/{zipped_file}'

        with zipfile.ZipFile(file_path, 'r') as zipped:  # Extracting
            zipped.extractall(f'{parent_dir}/extracted')

        os.remove(file_path) # removes zip files after the execution of the code

print('Extraction Ended')

# Reading Employees Names on Excel File and Converting them into a List

df_names = pd.read_excel('servidores.xlsx')
names_list = df_names['Nomes'].to_list()

# Looping Through Extracted Folder, Parsing the .xml File and Retrieving Information

dir_files = listdir_nohidden(parent_dir / 'extracted')  # gets all file names into the extracted folder
                                                        # had to use it because a system file (.DS_Store) was bugging
                                                        # the code


d = {'nome': [], 'arquivo': [], 'texto': []}    # dictionary to store data and later convert it into a Data Frame
                                                # and an Output Excel File


for xml_file in dir_files:

    tree = ET.parse(parent_dir / 'extracted' / xml_file)  # Parsing the XML file
    root = tree.getroot()  # Creating the root object

    text = root[0][0][5].text # retrieving the text from the XML file

    for name in names_list:
        if name.lower() in text.lower():
            d['nome'].append(name)
            d['arquivo'].append(xml_file)
            d['texto'].append(text)
        else:
            continue

output_df = pd.DataFrame(data=d)

output_df.to_excel('registros.xlsx', index=False)

print('Code Execution Ended')



