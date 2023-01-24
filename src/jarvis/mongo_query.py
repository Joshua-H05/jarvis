from pymongo import MongoClient
import pandas as pd
from jarvis import secret

link = secret.mongo_link
cluster = MongoClient(link)


def load_data(collection_name):
    db = cluster["jarvis_data"]
    collection = db[collection_name]
    cursor = collection.find()
    docs = []
    for document in cursor:
        docs.append(document)
    return docs


def dict_list_to_df(doc):
    reformatted = pd.DataFrame.from_dict(doc)
    return reformatted


def load_and_reformat(collection_name):
    doc = load_data(collection_name)
    reformatted = dict_list_to_df(doc)
    return reformatted


if __name__ == "__main__":
    df = load_and_reformat("suv_sales")
    print(df)