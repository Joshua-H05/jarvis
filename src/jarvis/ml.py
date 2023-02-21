import pandas as pd
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from pymongo import MongoClient
import pickle
import pysnooper
from jarvis import secret, mongo_query as mq


def train_log_reg(df, threshold):
    y = df["labels"]
    x = df[[col for col in list(df) if col not in ("labels", "ID", "_id")]]

    while True:
        x_train, x_test, y_train, y_test = train_test_split(x, y)

        log_reg = LogisticRegression()
        log_reg.fit(x_train, y_train)
        score = log_reg.score(x_test, y_test)
        if score > threshold:
            print(f"Ratio between 0's and 1's: {y_test.tolist().count('0') / y_test.tolist().count('1')}")
            print(score)
            print(log_reg.coef_)
            return log_reg, score


def train_log_reg_cv(df):
    y = df["labels"]
    x = df[[col for col in list(df) if col not in ("labels", "ID", "_id")]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    log_reg = LogisticRegressionCV(cv=5)
    log_reg.fit(x_train, y_train)
    y_pred = log_reg.predict(x_test)
    score = metrics.accuracy_score(y_test, y_pred)
    print(score)
    print(log_reg.predict(x_test))


def train_svm(df):
    y = df["labels"]
    x = df[[col for col in list(df) if col not in ("labels", "ID", "_id")]]
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    clf = svm.SVC(kernel='linear')
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    score = metrics.accuracy_score(y_test, y_pred)
    print(score)


def train_decision_tree():
    pass


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

def retrieve_model(model_name):
    db = cluster["jarvis_models"]
    col = db[model_name]
    data = col.find({"name": model_name})
    for i in data:
        json_data = i

    pickled_model = json_data[model_name]
    return pickle.loads(pickled_model)


def predict(model_name, df):
    x = df[[col for col in list(df) if col not in ("labels", "ID", "_id")]]
    model = retrieve_model(model_name)
    results = model.predict(x)
    return results


if __name__ == "__main__":
    """df = mq.load_and_reformat("cars")"""
    df = pd.read_csv("cars.csv")
    train_log_reg_cv(df)


