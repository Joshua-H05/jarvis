from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from jarvis import mongo_query as mq


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



if __name__ == "__main__":
    data = mq.load_and_reformat("cars")
    train_log_reg(data)
