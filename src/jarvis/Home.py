import streamlit as st

st.write("# 👋 This is Jarvis, your personal data analysis assistant!")
st.write("## Here's a quick guide on how to use me:")
st.markdown("This web application consists of four pages: Preprocessing, gui plot, gui ml and verbal interaction")
st.markdown(" * On the preprocessing page, you can perform basic data cleansing tasks "
            "and prepare your data for further analysis by dealing with missing values, removing rows and columns "
            "and performing one hot encoding, etc.")
st.markdown("* On the gui plot page, you can visualize data by creating histograms, pie charts and scatter plots")

st.markdown("* On the gui ml page, you can train either an SVM model or a logistic regression model "
            "Note: You have to name the model before training it")

st.markdown("* On the verbal interaction page, you can talk to me and ask me to perform tasks for you. "
            "Sadly, as I am not able to intelligently parse your speech, so when I ask you to choose "
            "between options I give you, you'll have to repeat the option word for word. Similarly, when I ask you "
            "for the name of a dataset or the name of a column in a dataset, "
            "please tell me without adding any other words")


# Sidebar section
st.sidebar.title("Select a function above! ⬆️")
