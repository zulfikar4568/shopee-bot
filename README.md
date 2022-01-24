## Install Dependencies
**Note: This script has been testing only in Ubuntu 20.04**
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install chromium-chromedriver
pip install --upgrade requests && pip3 install --upgrade requests
pip3 install -r dependencies.txt
````
## Rename your config

`config.py.example` to `config.py`

## Check Version of Python
```
python --version
python3 --version
```

## Running the Script
```
python3 shopee.py
```