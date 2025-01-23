import streamlit as st
import pandas as pd
import duckdb

st.write("""
 # SQL STR
 Spaced repetition System SQL Practice
""")

with st.sidebar:

    option = st.selectbox(
    "What would you like to review",
    ["Email", "Home phone", "Mobile phone"],
    index = None,
    placeholder= "Select a theme"
)

    st.write("You selected:", option)



data = {"a" : [1,2,3], "b" : [4,5,6], "c": [7,8,9]}
df = pd.DataFrame(data)


tab1, tab2, tab3 = st.tabs(["cat", "dog", "owl"])

with tab1:
    #st.header("A cat")
    #st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    my_query = st.text_area(label = "Entrer votre input")
    result = duckdb.query(my_query).df()
    st.write(f"Vous avez entrez la requête {my_query}")
    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

