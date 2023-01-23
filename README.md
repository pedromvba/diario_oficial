# Project Diário Oficial

## Description:

This project reads names stored in a Excel file and searches for them in the 2nd Section of the Diário Oficial da União 
(DOU). The DOU files are obtained on .xml thru InLabs site: https://inlabs.in.gov.br/acessar.php

## Content Table

1. [Description](#Description)
2. [Status](#Status)
3. [Requirements](#Requirements)
4. [Adjustments](#Adjustments)
5. [Limitations](#Limitations)
6. [Step by Step User Guide](#step-by-step-user-guide)
7. [Contact](#Contact)

## Status

Finished

## Requirements

1. Create an account in https://inlabs.in.gov.br/acessar.php
2. Save your login and password
3. Acess the github repository https://github.com/Imprensa-Nacional/inlabs/tree/master/public/python
4. Copy the inlabs-auto-download-xml.py code/file

## Adjustments

Upon inlabs-auto-download-xml.py

1. Replace variables login (your login will be an e-mail address) and senha (password) with your login and password 
created at https://inlabs.in.gov.br/acessar.php

```python
login = "email@dominio.com" # code line 4
senha = "minha_senha" # code line 5

login = "email address" # code line 4
senha = "password created" # code line 5
```

2. Select the section of the DOU you want to search

```python
tipo_dou="D01 D02 D03 D01E DO2E DO3E"  # code line 7

tipo_dou="D02"  # code line 7
```
3. Insert parameter verify = False in requests functions (2 cases)

This will disable, and therefore avoid, security certificate check in Python requests.

```python
response_arquivo = s.request("GET", url_arquivo, headers = cabecalho_arquivo) # code line 37
response_arquivo = s.request("GET", url_arquivo, headers = cabecalho_arquivo, verify=False) # code line 37

response = s.request("POST", url_login, data=payload, headers=headers) # code line 52
response = s.request("POST", url_login, data=payload, headers=headers, verify=False) # code line 52
```

4. Insert if __name__ == "__main__"

This will allow you to import the login function and start a fresh code in main.py

``` python
login() # code line 56

if __name__ == "__main__": # code line 56
    login() # codeline 57
```

5. Comment Out exit(0)

This will allow the code to continue after you executed the login function

``` python
exit(0) # code line 48
# exit(0) # code line 48

```

## Limitations

* Works only for the actual day. It does not check Diario Oficial files from other dates
* Employees names have to be on an excel file named "servidores.xlsx" with the column name as "Nomes"
* Code does not check for names written wrong or without the proper accentuation
* All files must be on the same directory where the python code will be executed
* After running, you have to manually delete the extracted folder. It could be done automatically, however keeping the 
folder allow you to double-check the information.

## Step by Step User Guide

1. Follow the [Requirements](#Requirements)
2. Make the [Adjustments](#Adjustments) in the inlabs_auto_download_xml.py or download the one from this repository 
which is already adjusted. If you download the one from this repository, remember to insert your login and password
credentials in inlabs_auto_download_xml.py, code lines 4 and 5.
3. Store the adjusted "inlabs_auto_download_xml.py" and the "servidores.xlsx" files with the employees names into the 
same folder as the python files.
4. Run the code
5. After running, delete the extracted folder so the files from the next execution will not be mixed with the 
previous ones.

## Contact

For further instructions or contributions, please send an e-mail to pedro.dataanalysis@gmail.com