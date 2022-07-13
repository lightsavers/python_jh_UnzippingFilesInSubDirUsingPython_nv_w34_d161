import os
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import requests

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/IndoorMovement.zip"
content = requests.get(url)
zf = ZipFile(BytesIO(content.content))

zf.namelist()

#dfs += [pd.read_csv(zf.open('*.csv')]

dfs = []

with ZipFile(BytesIO(content.content)) as z:    
    for filename in zf.namelist():
        if zf.is_dir():
            # read the file
            if filename.endswith('.csv'):
                for line in zf.open(filename):
                    #df = pd.read_csv(zf.open(line))
                    #print(line.decode('utf-8'))
                    
                    #zip_file = os.path.join(zf, filename)
                    #zf = zipfile.ZipFile(zip_file)
                    dfs += [pd.read_csv(zf.open('*.csv'), header=None, sep=";", encoding='latin1') for f in zf.namelist()]

df = pd.concat(dfs,ignore_index=True)
