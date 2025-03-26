import streamlit as st
import sidebar
import textPage
import imagePage

# Main page routing
page = sidebar.show()

if page == "Text":
    textPage.renderPage()
elif page == "Image":
    imagePage.renderPage()
