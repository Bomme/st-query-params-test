import streamlit as st

if "some_string" not in st.session_state:
  params = st.experimental_get_query_params()

st.write(params)
