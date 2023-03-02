import streamlit as st

from jarvis import mongo_query as mq
from jarvis import mongodb_atlas_store_files as ms
from jarvis import compute


def sidebar_list_ds():
    datasets = mq.list_all_collections()
    st.sidebar.radio("Choose a dataset!", datasets, key="selected_file")
    print(type(st.session_state))


# Main section

def select_plot_type():
    plot_types = ["Pie Chart", "Histogram", "Scatter Plot"]
    st.selectbox("Select the type of graph you would like to create!", plot_types, key="plot_type")
    if st.session_state.plot_type == "Scatter Plot":
        double_plot_var()
    else:
        single_plot_var()


def single_plot_var():
    df = mq.load_and_reformat(st.session_state.selected_file)
    columns = mq.list_all_columns(df)
    st.selectbox(label="Choose the value you would like to plot", options=columns, key="col")


def double_plot_var():
    df = mq.load_and_reformat(st.session_state.selected_file)
    columns = mq.list_all_columns(df)
    st.selectbox(label="Choose the X axis for the plot", options=columns, key="x_axis")
    st.selectbox(label="Choose the Y axis for the plot", options=columns, key="y_axis")


def parse_func():
    df = mq.load_and_reformat(st.session_state.selected_file)
    if st.session_state.plot_type == "Histogram" and st.session_state.col:
        compute.plot_histogram(df, st.session_state.col)

    if st.session_state.plot_type == "Pie Chart" and st.session_state.col:
        compute.plot_pie_chart(df, st.session_state.col)

    if st.session_state.plot_type == "Scatter Plot" and st.session_state.x_axis and st.session_state.y_axis:
        x = st.session_state.x_axis
        y = st.session_state.y_axis
        compute.plot_scatter_plot(df, x_var=x, y_var=y)


if __name__ == "__main__":
    # sidebar
    user_file = st.sidebar.file_uploader("Upload your file here!")
    if user_file:
        if st.sidebar.button("Save your file in the database?"):
            ms.store_uploaded_file(file=user_file, ds_name=str(user_file.name))

    sidebar_list_ds()
    select_plot_type()
    parse_func()