# ui/output.py
import streamlit as st
from backend.rewrite_post import (
    improve_hook,
    strengthen_cta,
    shorten_post,
    make_bold
)

def render_output():
    st.subheader("Generated Post")

    if not st.session_state.generated_post:
        st.info("Use the sidebar to configure settings and click **Generate**.")
        return

    st.text_area(
        label="",
        value=st.session_state.generated_post,
        height=320
    )

    st.divider()
    st.markdown("**Refine Post**")

    _rewrite_toolbar()
    _undo_redo_controls()


def _rewrite_toolbar():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        _rewrite_button("🔁 Hook", improve_hook, "Hook improved ✨")

    with col2:
        _rewrite_button("🎯 CTA", strengthen_cta, "CTA strengthened ✨")

    with col3:
        _rewrite_button("✂ Shorten", shorten_post, "Post shortened ✨")

    with col4:
        _rewrite_button("🔥 Bold", make_bold, "Tone made bolder ✨")


def _rewrite_button(label, rewrite_fn, toast_msg):
    if st.button(label, use_container_width=True):
        st.session_state.history.append(st.session_state.generated_post)
        st.session_state.future.clear()
        st.session_state.generated_post = rewrite_fn(
            st.session_state.generated_post
        )
        st.toast(toast_msg)
        st.rerun()


def _undo_redo_controls():
    undo_available = len(st.session_state.history) > 0
    redo_available = len(st.session_state.future) > 0

    col1, col2 = st.columns(2)

    with col1:
        if st.button("↩ Undo", disabled=not undo_available, use_container_width=True):
            st.session_state.future.append(st.session_state.generated_post)
            st.session_state.generated_post = st.session_state.history.pop()
            st.toast("Undo successful ⏪")
            st.rerun()

    with col2:
        if st.button("↪ Redo", disabled=not redo_available, use_container_width=True):
            st.session_state.history.append(st.session_state.generated_post)
            st.session_state.generated_post = st.session_state.future.pop()
            st.toast("Redo successful ⏩")
            st.rerun()

    st.caption("Undo/Redo applies only to rewrite actions")