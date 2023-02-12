from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from pymongo import MongoClient
import pickle

from jarvis import secret, mongo_query as mq


def train_log_reg(df):
    y = df["labels"]
    x = df[[col for col in list(df) if col not in ("labels", "ID", "_id")]]
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    log_reg = LogisticRegression()
    log_reg.fit(x_train, y_train)
    log_reg.fit(x_train, y_train)
    print(log_reg.coef_)
    score = log_reg.score(x_test, y_test)
    print(score)
    return log_reg, score


link = secret.mongo_link
cluster = MongoClient(link)


def store_ml_model(model, model_name):
    db = cluster["jarvis_models"]
    col = db[model_name]
    pickled_model = pickle.dumps(model)
    info = col.insert_one({model_name: pickled_model, "name": model_name})
    details = {
        'inserted_id': info.inserted_id,
        "model_name": model_name,
    }
    return details
# https://medium.com/up-engineering/saving-ml-and-dl-models-in-mongodb-using-python-f0bbbae256f0


if __name__ == "__main__":
    data = mq.load_and_reformat("cars")
    model, score = train_log_reg(data)
    if score >= 0.7:
        store_ml_model(model=model, model_name="cars logistic regression")
