"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://github.com/nickeubank/practicaldatascience/blob/master/Example_Data/world-small.csv", 
            file_path="data/world-small.csv"):
    """"Extract a url to a file path"""
    timeout = 100
    with requests.get(url, timeout=timeout) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path

extract()