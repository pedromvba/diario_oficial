# Imports
from inlabs_auto_download_xml import login
import zipfile
from pathlib import Path
import os

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

with zipfile.ZipFile('/Users/pedromonteiro/Library/Mobile Documents/com~apple~CloudDocs/dsProjects/Diario_Oficial/2023-01-13-DO2.zip', 'r') as zipped: # Extracting
    zipped.extractall(folder_dir/'extracted')

print('File Extracted')







# Delete zip file and the extract folder at the end
