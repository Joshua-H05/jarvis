import streamlit as st

from jarvis import mongo_query as mq
from jarvis import mongodb_atlas_store_files as ms
from jarvis import compute

st.set_page_config(layout="wide")

a1, a2, a3 = st.columns(3)

b1, b2 = st.columns(2, gap="large")

st.markdown("#\n #")

c1, c2 = st.columns(2, gap="large")



def single_plot_var(plot_type):
    df = mq.load_and_reformat(st.session_state.selected_file)
    columns = mq.list_all_columns(df)
    st.selectbox(label="Choose the value you would like to plot", options=columns, key=f"col_{plot_type}")


def double_plot_var(plot_type):
    df = mq.load_and_reformat(st.session_state.selected_file)
    columns = mq.list_all_columns(df)
    st.selectbox(label="Choose the X axis for the plot", options=columns, key=f"x_axis_{plot_type}")
    st.selectbox(label="Choose the Y axis for the plot", options=columns, key=f"y_axis_{plot_type}")


def graphs():
    df = mq.load_and_reformat(st.session_state.selected_file)
    with b1:
        st.markdown("## Histogram")
        single_plot_var("hist")
        try:
            compute.plot_histogram(df, st.session_state.col_hist, st_col=b1)
        except TypeError:
            st.warning("Sorry, but we could not plot the data you have selected. Please try something else.")
    with b2:
        st.markdown("## Pie Chart")
        single_plot_var("pie")
        try:
            compute.plot_pie_chart(df, st.session_state.col_pie, st_col=b2)
        except TypeError:
            st.warning("Sorry, but we could not plot the data you have selected. Please try something else.")

    with c1:
        st.markdown("## Scatterplot")
        double_plot_var("scatter")
        try:
            x = st.session_state.x_axis_scatter
            y = st.session_state.y_axis_scatter
            compute.plot_scatter_plot(df, x_var=x, y_var=y, st_col=c1)
        except TypeError:
            st.warning("Sorry, but we could not plot the data you have selected. Please try something else.")
    with c2:
        st.markdown("## Bar Chart")
        double_plot_var("bar")
        try:
            x = st.session_state.x_axis_bar
            y = st.session_state.y_axis_bar
            compute.plot_bar_chart(df, x=x, y=y, st_col=c2)
        except TypeError:
            st.warning("Sorry, but we could not plot the data you have selected. Please try something else.")


def sidebar_list_ds():
    datasets = mq.list_all_collections()
    st.sidebar.radio("Choose a dataset!", datasets, key="selected_file")
    cols = mq.list_all_columns(mq.load_and_reformat(st.session_state.selected_file))
    st.sidebar.selectbox("Choose a column for your metrics!", cols,  key="metric_col")

def metrics():
    df = mq.load_and_reformat(st.session_state.selected_file)
    col = st.session_state.metric_col
    try:
        a1.metric("Mean", compute.compute_mean(df, col))
        a2.metric("Mode", compute.compute_mode(df, col))
        a3.metric("Median", compute.compute_median(df, col))
    except TypeError:
        st.sidebar.warning("Sorry, but we could not plot the data you have selected. Please try something else.")


if __name__ == "__main__":
    # sidebar
    user_file = st.sidebar.file_uploader("Upload your file here!")
    if user_file:
        if st.sidebar.button("Save your file in the database?"):
            ms.store_uploaded_file(file=user_file, ds_name=str(user_file.name))

    sidebar_list_ds()
    metrics()
    graphs()


