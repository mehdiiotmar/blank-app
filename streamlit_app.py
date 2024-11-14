import streamlit as st
# CSS pour masquer l'icône GitHub
hide_github_icon = """
<style>
.viewerBadge_container__1QSob { display: none !important; }
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
st.title("🎈 My new app")
st.write(
    "hello mehdi "
)
