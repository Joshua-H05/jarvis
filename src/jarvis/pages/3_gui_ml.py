import streamlit as st
from jarvis import ml
from jarvis import mongo_query as mq
from jarvis import mongodb_atlas_store_files as ms


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
    st.session_state = st.selectbox("Select the algorithm you would like to use!", algos, key="model_type")


def train_model():
    df = mq.load_and_reformat(st.session_state.selected_file)
    if st.button("Train Model!"):
        if st.session_state.model_type == "Logistic Regression":
            model, score = ml.train_log_reg_cv(df)
            st.session_state.trained_model = model
            st.write(f"The test accuracy of the model was: {score}")
            st.session_state["trained"] = True

        if st.session_state.model_type == "Support Vector Machine":
            model, score = ml.train_svm(df)
            st.session_state.trained_model = model
            st.write(f"The test accuracy of the model was: {score}")
            st.session_state["trained"] = True


def save_model():
    if st.checkbox("Save the model?"):
        name = st.text_input
        if name and st.session_state.model:
            ml.store_ml_model(model=st.session_state.model, model_name=name)


# Prediction section
def select_model():
    models = ml.list_all_models()
    models.append("Previously trained model")
    st.session_state = st.selectbox("Select the model you would like to use!", models, key="model")


def predict():
    if st.session_state.model and st.session_state.selected_file:
        if st.session_state.model == "Previously trained model":
            model = st.session_state.trained_model
        else:
            model = ml.retrieve_model(st.session_state.model)
        df = mq.load_and_reformat(st.session_state.selected_file)
        results = ml.predict(model, df)
        st.dataframe(results)


if __name__ == "__main__":
    sidebar()
    st.title("Train A Model!")
    select_train_model()
    train_model()
    save_model()

    st.title("Perform A prediction!")
