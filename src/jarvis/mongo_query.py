# citation complete
from pymongo import MongoClient
import pandas as pd
import streamlit as st

link = st.secrets["mongo"]["mongo_link"]
cluster = MongoClient(link)


def load_data(collection_name):
    db = cluster["jarvis_data"]
    collection = db[collection_name]
    cursor = collection.find()
    docs = []
    for document in cursor:
        docs.append(document)
    return docs

# Derived from source: https://www.mongodb.com/docs/manual/tutorial/query-documents/
# Last accessed Jan 19, 2023

def dict_list_to_df(doc):
    reformatted = pd.DataFrame.from_dict(doc)
    return reformatted

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
# Last accessed Jan 25, 2023


def load_and_reformat(collection_name):
    doc = load_data(collection_name)
    reformatted = dict_list_to_df(doc)
    reformatted.drop(columns="_id", inplace=True)
    return reformatted
# Derived from source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
# Last accessed Jan 25, 2023



def list_all_collections():
    collections = cluster["jarvis_data"].list_collection_names()
    return collections
# Derived from source: https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html
# Last accessed Jan 25, 2023


def list_all_columns(df):
    column_list = list(df.columns.values.tolist())
    return column_list
# Copied from tutorial: https://sparkbyexamples.com/pandas/conver-pandas-column-to-list/
# Last accessed Jan 25, 2023


if __name__ == "__main__":
    df = load_and_reformat("cars")
    list_all_collections()
    print(list_all_columns(df))
