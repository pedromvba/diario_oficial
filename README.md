# Project Diário Oficial

## Description:

This project reads names stored in a Excel file and searches for them in the 2nd Section of the Diário Oficial da União 
(DOU). The DOU files are obtained on .xml thru InLabs site: https://inlabs.in.gov.br/acessar.php

## Content Table

1. [Description](#Description)
2. [Status](#Status)
3. [Requirements](#Requirements)
4. [Adjustments in inlabs-auto-download-xml.py](#Adjustments in inlabs-auto-download-xml.py)

## Status

In development

## Requirements

1. Create an account in https://inlabs.in.gov.br/acessar.php
2. Save your login and password
3. Acess the github repository https://github.com/Imprensa-Nacional/inlabs/tree/master/public/python
4. Copy the inlabs-auto-download-xml.py code/file

## Adjustments in inlabs-auto-download-xml.py

1. Replace variables login (your login will be an e-mail address) and senha (password) with your login and password created at https://inlabs.in.gov.br/acessar.php

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

``` python
login() # code line 56

if __name__ == "__main__": # code line 56
    login() # codeline 57
```
   