import streamlit as st
from backend.few_shot import FewShotPosts
from backend.post_generator import generate_post

from state.session import init_session_state
from ui.sidebar import render_sidebar
from ui.output import render_output


def main():
    st.title("LinkedIn Post Generator")
    st.caption("Create, refine, and optimize LinkedIn posts with AI")
    st.divider()

    fs = FewShotPosts()
    init_session_state()

    config = render_sidebar(fs)

    if config["generate"]:
        with st.spinner("Generating your post..."):
            st.session_state.generated_post = generate_post(
                config["length"],
                config["language"],
                config["tag"],
                config["audience"],
                config["goal"],
                config["style"],
                config["emoji"],
                config["hashtags"]
            )
            st.session_state.history.clear()
            st.session_state.future.clear()
        st.rerun()

    if config["clear"]:
        st.session_state.generated_post = ""
        st.session_state.history.clear()
        st.session_state.future.clear()
        st.rerun()

    render_output()


if __name__ == "__main__":
    main()