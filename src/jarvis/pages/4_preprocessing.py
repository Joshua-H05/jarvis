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
    with st.container():
        st.dataframe(df, height=80)


def ohe(df):
    st.subheader("One Hot Encoding")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Encode!", cols)

    for col in selected:
        df = p.one_hot(df, col)
        print(df)
    show_df(df)


def rm_col(df):
    st.subheader("Remove Columns")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Remove!", cols)

    for col in selected:
        df = p.rm_col(df, col)
    show_df(df)

@pysnooper.snoop()
def rm_row(df):
    st.subheader("Remove Rows")
    unwanted = st.text_input("Type in the indices of all the rows you would like to remove, separated with commas:")
    if unwanted:
        unwanted.split(",")
        result = p.rm_row(df, [int(i) for i in unwanted])
        show_df(result)


# Not tested yet
def replace(df):
    st.subheader("Remove Missing Values")
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


def op(df):
    try:
        st.subheader("Feature Engineering")
        cols = mq.list_all_columns(df)
        ops = ("+", "-", "*", "/")
        first = st.selectbox("Select the first column", options=cols)
        second = st.selectbox("Select the second column", options=cols)
        operator = st.selectbox("Select the operation you would like to perform", options=ops)
        name = st.text_input("What would you like to call the new column?")
        if first and second and operator and name:
            result = p.operation(df=df, name=name, operator=operator, col1=first, col2=second)
            show_df(result)
    except ValueError:
        st.warning("Sorry, but we can't seem to engineer this feature. Please pick another one.")


if __name__ == "__main__":
    sidebar()
    name = st.session_state.selected_file
    df = mq.load_and_reformat(name)
    show_df(df)
    with st.container():
        rm_col(df)
        rm_row(df)
    with st.container():
        replace(df)
        op(df)
    ohe(df)
