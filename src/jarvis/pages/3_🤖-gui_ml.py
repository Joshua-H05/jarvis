# All functions followed by "st." leverage streamlit. The sole source consulted was the official documentation
# provided by Streamlit: https://docs.streamlit.io

import streamlit as st
from streamlit_elements import elements, mui, html
import os

from jarvis import ml
from jarvis import mongo_query as mq
from jarvis import mongodb_atlas_store_files as ms
import pysnooper

CWD = os.getcwd()

def sidebar_list_ds():
    datasets = mq.list_all_collections()
    st.sidebar.radio("Choose a dataset!", datasets, key="selected_file")


def sidebar():
    user_file = st.sidebar.file_uploader("Upload your file here!")
    if user_file:
        if st.sidebar.button("Save your file in the database?"):
            ms.store_uploaded_file(file=user_file, ds_name=str(user_file.name))
    sidebar_list_ds()


# training section

def select_train_model():
    algos = ["Logistic Regression", "Support Vector Machine"]
    st.session_state["model_type"] = st.selectbox("Select the algorithm you would like to use!", algos, key="plot_type")


def train_model():
    df = mq.load_and_reformat(st.session_state.selected_file)
    select_train_model()
    name = st.text_input(" What would you like to call this model?")
    if st.button("Train Model!"):
        if st.session_state.model_type == "Logistic Regression":
            model, score = ml.train_log_reg_cv(df)
            st.session_state["model"] = model
            st.write(f"The test accuracy of the model was: {score}")

        elif st.session_state.model_type == "Support Vector Machine":
            model, score = ml.train_svm(df)
            st.session_state["model"] = model
            st.write(f"The test accuracy of the model was: {score}")

    if st.button("Save the model?"):
        details = ml.store_ml_model(model=st.session_state.model, model_name=name)
        st.write("model saved")
        print(details)

    else:
        print("Button not pressed")


def save_model():
    if st.button("Save the model?"):
        name = st.text_input(" What would you like to call this model?")
        if name and st.session_state.model:
            details = ml.store_ml_model(model=st.session_state.model, model_name=st.session_state["model_name"])
            print(details)


@pysnooper.snoop(depth=2)
def select_model():
    models = ml.list_all_models()
    st.selectbox("Select the model you would like to use!", models, key="use_model")


def predict():
    if st.session_state.selected_file:
        df = mq.load_and_reformat(st.session_state.selected_file)
        if st.session_state.use_model:
            try:
                model = st.session_state.use_model
                result = ml.predict_stored_model(model, df)
                st.dataframe(result)
            except ValueError:
                st.warning("Sorry, but some of the columns in the dataset you selected seem to be of the wrong type. "
                           "You may have to reengineer some of your features")


if __name__ == "__main__":
    with open(f'{CWD}/src/jarvis/assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    sidebar()

    with elements("new_element"):
        st.title("Train A Model!")
        train_model()

    with elements("newer_element"):
        st.title("Perform a prediction")
        select_model()
        predict()
