import pandas
import plotly.express as px 
import csv 
import numpy as np

def getDataSource(data_path):
    coffeeInMl  = []
    sleepInHours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffeeInMl.append(float(row["Coffee in ml"]))
            sleepInHours.append(float(row["sleep in hours"]))

    return {"x":sleepInHours,"y":coffeeInMl}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between sleep in hours  and coffe in ml:\n-->",correlation[0,1])

def setup():
    data_path = "data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()