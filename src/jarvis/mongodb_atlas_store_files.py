import csv
from pymongo import MongoClient
from jarvis import secret


link = secret.mongo_link
cluster = MongoClient(link)

db = cluster["jarvis_data"]
suv_sales_col = db["cars"]

suv_data = []
with open("suv_data.csv", newline='') as suv:
    suv_dict = csv.DictReader(suv)
    for row in suv_dict:
        suv_data.append(row)

print(suv_data)

suv_sales_col.insert_many(suv_data)
