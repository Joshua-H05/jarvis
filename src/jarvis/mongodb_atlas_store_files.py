import csv
from pymongo import MongoClient
from jarvis import secret
import pandas as pd

link = secret.mongo_link
cluster = MongoClient(link)


def save_ds(ds_name, file):
    with open(file) as f:
        dict_data = csv.DictReader(f)
        save(ds_name, dict_data)


def save(df_name, data):
    db = cluster["jarvis_data"]
    col = db[df_name]

    data = [row for row in data]
    col.insert_many(data)


# function copied from streamlit https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
def store_uploaded_file(file, ds_name):
    db = cluster["jarvis_data"]
    col = db[ds_name]

    df = pd.read_csv(file)
    df_reformat = df.to_dict(orient="records")
    dict_list = []
    for row in df_reformat:
        print(row)
        dict_list.append(row)
    col.insert_many(dict_list)


if __name__ == "__main__":
    save_ds(ds_name="customers", file="data/customer.csv")
