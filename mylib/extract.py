"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests
a = "https://raw.githubusercontent.com/Barabasi-Lab/"
b = "GroceryDB/main/data/GroceryDB_IgFPro.csv"
c = a + b
def extract(url= c, 
            file_path="data/GroceryDB_IgFPro.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path
