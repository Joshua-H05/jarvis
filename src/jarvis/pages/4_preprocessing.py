import streamlit as st
from jarvis import preprocessing as p
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


def show_df(df):
    st.dataframe(df, height=60)


def ohe():
    name = st.session_state.selected_file # these lines are repetitive, need to clean up
    df = mq.load_and_reformat(name)
    st.title("One Hot Encoding")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Encode!", cols)

    for col in selected:
        df = p.one_hot(df, col)
        print(df)
    show_df(df)

def rm():
    pass





if __name__ == "__main__":
    sidebar()
    df = mq.load_and_reformat(st.session_state.selected_file)
    show_df(df)
    ohe()
