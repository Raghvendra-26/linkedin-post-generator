# state/session.py
import streamlit as st

def init_session_state():
    if "generated_post" not in st.session_state:
        st.session_state.generated_post = ""

    if "history" not in st.session_state:
        st.session_state.history = []   # undo stack

    if "future" not in st.session_state:
        st.session_state.future = []    # redo stack
