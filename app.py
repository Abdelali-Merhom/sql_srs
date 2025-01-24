import streamlit as st
import pandas as pd
import duckdb
import io



csv = '''
beverage,price
orange juice, 2.5
Expressio, 2
Tea, 3
'''
beverages = pd.read_csv(io.StringIO(csv))

<<<<<<< HEAD
csv2 = '''
food_item, food_price
cookie juice, 2.5
chocolat, 2
muffin, 3
'''
food_items = pd.read_csv(io.StringIO(csv2))
=======



>>>>>>> 417f8bc (Ajout sidebar)


answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = duckdb.sql(answer).df()

<<<<<<< HEAD
st.header("Entrer votre code:")
query = st.text_area(label = "Votre code SQL ici", key = "user_input")
=======
data = {"a" : [1,2,3], "b" : [4,5,6], "c": [7,8,9]}
df = pd.DataFrame(data)
>>>>>>> 417f8bc (Ajout sidebar)

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)

with st.sidebar:

    option = st.selectbox(
    "What would you like to review",
    ["Email", "Home phone", "Mobile phone"],
    index = None,
    placeholder= "Select a theme"
    )
    st.write("You selected:", option)


