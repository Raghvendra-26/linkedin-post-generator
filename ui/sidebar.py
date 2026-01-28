# ui/sidebar.py
import streamlit as st
from constants import (
    LENGTH_OPTIONS,
    LANGUAGE_OPTIONS,
    AUDIENCE_OPTIONS,
    GOAL_OPTIONS,
    STYLE_OPTIONS
)

def render_sidebar(fs):
    with st.sidebar:
        st.header("Post Settings")

        selected_tag = st.selectbox("Topic", fs.get_tags())
        selected_length = st.selectbox("Length", LENGTH_OPTIONS)
        selected_language = st.selectbox("Language", LANGUAGE_OPTIONS)

        selected_audience = st.selectbox("Audience", AUDIENCE_OPTIONS)
        selected_goal = st.selectbox("Goal", GOAL_OPTIONS)
        selected_style = st.selectbox("Style", STYLE_OPTIONS)

        st.divider()

        st.subheader("Advanced Options")
        emoji = st.checkbox("Enable Emojis")
        hashtags = st.checkbox("Add Hashtags")

        st.divider()

        generate = st.button("🚀 Generate", use_container_width=True)
        clear = st.button(
            "🧹 Clear",
            use_container_width=True,
            disabled=not bool(st.session_state.generated_post)
        )

    return {
        "tag": selected_tag,
        "length": selected_length,
        "language": selected_language,
        "audience": selected_audience,
        "goal": selected_goal,
        "style": selected_style,
        "emoji": emoji,
        "hashtags": hashtags,
        "generate": generate,
        "clear": clear,
    }
