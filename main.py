import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from rewrite_post import (
    improve_hook,
    strengthen_cta,
    shorten_post,
    make_bold
)

length_options = ['Short','Medium','Long']
language_options = ['English','Hinglish']
audience_options = ['Student','Fresher','Professional','Founder','Recruiter']
goal_options = ['Job Search','Personal Branding','Thought Leadership','Hiring','Networking']
style_options = ['Conversational','Corporate','Storytelling','Data-driven','Bold']


def main():
    # -----------------------------
    # Header
    # -----------------------------
    st.title("LinkedIn Post Generator")
    st.caption("Create, refine, and optimize LinkedIn posts with AI")
    st.divider()

    fs = FewShotPosts()

    if "generated_post" not in st.session_state:
        st.session_state.generated_post = ""

    # -----------------------------
    # Post Settings
    # -----------------------------
    st.subheader("Post Settings")

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_tag = st.selectbox("Topic", options=fs.get_tags())
        with col2:
            selected_length = st.selectbox("Length", options=length_options)
        with col3:
            selected_language = st.selectbox("Language", options=language_options)

        col1, col2, col3 = st.columns(3)
        with col1:
            selected_audience = st.selectbox("Audience", options=audience_options)
        with col2:
            selected_goal = st.selectbox("Goal", options=goal_options)
        with col3:
            selected_style = st.selectbox("Style", options=style_options)

    # -----------------------------
    # Advanced Options (Cleaner UI)
    # -----------------------------
    with st.expander("Advanced Options"):
        emoji = st.checkbox("Enable Emojis")
        hashtags = st.checkbox("Add Hashtags")

    # -----------------------------
    # Actions
    # -----------------------------
    st.subheader("Actions")

    post_exists = bool(st.session_state.get("generated_post"))

    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("🚀 Generate", use_container_width=True):
            with st.spinner("Generating your post..."):
                st.session_state.generated_post = generate_post(
                    selected_length,
                    selected_language,
                    selected_tag,
                    selected_audience,
                    selected_goal,
                    selected_style,
                    emoji,
                    hashtags
                )
            st.rerun()

    with col2:
        if st.button(
            "🧹 Clear",
            disabled=not post_exists,
            use_container_width=True
        ):
            st.session_state.generated_post = ""
            st.rerun()

    st.divider()

    # -----------------------------
    # Output Section
    # -----------------------------
    st.subheader("Generated Post")

    if st.session_state.generated_post:
        st.text_area(
            label="",
            value=st.session_state.generated_post,
            height=320
        )

        st.caption("Tip: Use rewrite options to refine instead of regenerating")

        # -----------------------------
        # Rewrite Toolbar
        # -----------------------------
        st.markdown("**Refine Post**")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("🔁 Hook", use_container_width=True):
                st.session_state.generated_post = improve_hook(
                    st.session_state.generated_post
                )
                st.toast("Hook improved ✨")
                st.rerun()

        with col2:
            if st.button("🎯 CTA", use_container_width=True):
                st.session_state.generated_post = strengthen_cta(
                    st.session_state.generated_post
                )
                st.toast("CTA strengthened ✨")
                st.rerun()

        with col3:
            if st.button("✂ Shorten", use_container_width=True):
                st.session_state.generated_post = shorten_post(
                    st.session_state.generated_post
                )
                st.toast("Post shortened ✨")
                st.rerun()

        with col4:
            if st.button("🔥 Bold", use_container_width=True):
                st.session_state.generated_post = make_bold(
                    st.session_state.generated_post
                )
                st.toast("Tone made bolder ✨")
                st.rerun()

    else:
        st.info("Select options above and click **Generate** to create a post.")

if __name__ == "__main__":
    main()