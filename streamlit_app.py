import logging

import streamlit as st

params = st.experimental_get_query_params()
logging.info(f"{params=}")
if "my-field" not in params:
    st.session_state["MY_FIELD"] = "some default value"

params_second = st.experimental_get_query_params()
if "MY_FIELD" in st.session_state:
    logging.info(f"{params_second=} {st.session_state['MY_FIELD']=}")
else:
    logging.info(f"{params_second=}")

st.write(params)
