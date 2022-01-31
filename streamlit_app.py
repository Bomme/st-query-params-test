import logging

import streamlit as st

import separate_script

params = st.experimental_get_query_params()
logging.info(f"{params=}")
if not params:
  st.session_state["MY_FIELD"] = "some value"

params_separate = separate_script.get_query_params()
if "MY_FIELD" in st.session_state:
  logging.info(f"{params_separate=} {st.session_state['MY_FIELD']=}")
else:
  logging.info(f"{params_separate=}")

st.write("Main script")
st.write(params)

st.write("separate script")
st.write(params_separate)
