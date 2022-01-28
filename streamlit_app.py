import streamlit as st

import separate_script

params = st.experimental_get_query_params()
params_separate = separate_script.get_query_params()

st.write("Main script")
st.write(params)

st.write("separate script")
st.write(params_separate)
