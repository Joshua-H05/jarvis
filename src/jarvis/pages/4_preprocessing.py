import pysnooper
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
    st.dataframe(df, height=80)


def ohe():
    name = st.session_state.selected_file  # these lines are repetitive, need to clean up
    df = mq.load_and_reformat(name)
    st.title("One Hot Encoding")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Encode!", cols)

    for col in selected:
        df = p.one_hot(df, col)
        print(df)
    show_df(df)


def rm_col():
    name = st.session_state.selected_file  # these lines are repetitive, need to clean up
    df = mq.load_and_reformat(name)
    st.title("Remove Columns")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Remove!", cols)

    for col in selected:
        df = p.rm_col(df, col)
    show_df(df)


def rm_row():
    pass


# Not tested yet
@pysnooper.snoop()
def replace():
    name = st.session_state.selected_file  # these lines are repetitive, need to clean up
    df = mq.load_and_reformat(name)
    st.title("Remove Missing Values")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Edit!", cols)
    options = {"Drop Columns With Missing Values": "drop",
               "Replace Missing Values With Zeros": "zeros",
               "Replace Missing Values With The Mean Value Of The Column": "mean",
               "Replace Missing Values With The Median Value Of The Column": "median",
               }
    option = st.radio(label="Select The Method You Would Like To Use", options=options.keys())
    if st.button("Apply Changes!"):
        result = p.replace(df, selected, options[option])
        show_df(result)

        if result.equals(df):  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html
            st.write("No Missing Values!")
        else:
            st.write("Changes Applied!")


def op():
    name = st.session_state.selected_file  # these lines are repetitive, need to clean up
    df = mq.load_and_reformat(name)
    st.title("Feature Engineering")
    cols = mq.list_all_columns(df)
    ops = ("+", "-", "*", "/")
    first = st.selectbox("Select the first column", options=cols)
    second = st.selectbox("Select the second column", options=cols)
    operator = st.selectbox("Select the operation you would like to perform", options=ops)
    name = st.text_input("What would you like to call the new column?")
    result = p.operation(df=df, name=name, operator=operator, col1=first, col2=second)
    show_df(result)


if __name__ == "__main__":
    sidebar()
    df = mq.load_and_reformat(st.session_state.selected_file)
    show_df(df)
    ohe()
    rm_col()
    replace()
    op()
