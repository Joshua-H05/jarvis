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


def ohe():
    df = st.session_state["df"]
    st.subheader("One Hot Encoding")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Encode!", cols)

    for col in selected:
        df = p.one_hot(df, col)
        print(df)
    st.dataframe(df, height=80)
    st.session_state["df"] = df


def rm_col():
    df = st.session_state["df"]
    st.subheader("Remove Columns")
    cols = mq.list_all_columns(df)
    selected = st.multiselect("Select The Columns You Would Like To Remove!", cols)

    df = p.rm_col(df, selected)
    st.dataframe(df, height=80)
    st.session_state["df"] = df


@pysnooper.snoop()
def rm_row():
    df = st.session_state["df"]
    st.subheader("Remove Rows")
    unwanted = st.text_input("Type in the indices of all the rows you would like to remove, separated with commas:")
    print(type(unwanted))
    if unwanted:
        unwanted = unwanted.split(",")
        result = p.rm_row(df, [int(i) for i in unwanted])
        st.dataframe(result, height=80)
        st.session_state["df"] = result


# Not tested yet
def replace():
    df = st.session_state["df"]
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
        st.dataframe(result, height=80)
        st.session_state["df"] = result
        if result.equals(df):  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html
            st.success("Data appears to be complete!")
        else:
            st.success("Changes Applied!")


def op():
    df = st.session_state["df"]
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
            st.dataframe(result, height=80)
            st.session_state["df"] = result
    except ValueError:
        st.warning("Sorry, but we can't seem to engineer this feature. Please pick another one.")


def save():
    file_name = st.text_input("What would you like to name your file?")
    if st.button("Save your file?"):
        data = st.session_state["df"].to_dict(orient="records")
        ms.save(file_name, data)


if __name__ == "__main__":
    sidebar()
    name = st.session_state.selected_file
    st.session_state["df"] = mq.load_and_reformat(name)
    df = st.session_state["df"]
    st.dataframe(df, height=80)
    rm_col()
    rm_row()
    replace()
    op()
    ohe()
    save()
