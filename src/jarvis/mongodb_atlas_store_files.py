import csv
from pymongo import MongoClient
from jarvis import secret


link = secret.mongo_link
cluster = MongoClient(link)


def save_ds(ds_name, filepath):
    db = cluster["jarvis_data"]
    col = db[ds_name]

    data = []
    with open(filepath, newline='') as f:
        dict_data = csv.DictReader(f)
        for row in dict_data:
            data.append(row)
    col.insert_many(data)


if __name__ == "__main__":
    save_ds(ds_name="cars", filepath="cars.csv")
