import os
import csv

File="points.csv"
fields=["computer","player"]

def intialize_csv():
    if not os.path.exists(File):
        with open(File,"w",newline="") as f:
            csv.DictWriter(f,fieldnames=fields).writeheader()

def load_data():
    try:
        with open(File,"r",newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []
    
def save_points(data):
    with open(File,"a",newline="") as f:
         csv.DictWriter(f,fieldnames=fields).writerows(data)
         