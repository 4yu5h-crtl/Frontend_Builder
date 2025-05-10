import streamlit as st
import os
import sys

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import utility functions
from utils.init import init_session_state, load_custom_css, setup_page_config
from utils.api import generate_html_with_ai
from utils.project import save_project, load_project, list_projects

# Initialize the application
setup_page_config()
init_session_state()
load_custom_css()

# Test the application
st.title("DeepSite Test")

# Test session state
st.subheader("Session State")
st.write("API Key:", st.session_state.api_key)
st.write("HTML Content Length:", len(st.session_state.html_content))
st.write("Prompt History:", st.session_state.prompt_history)
st.write("Is Generating:", st.session_state.is_generating)
st.write("Current Project:", st.session_state.current_project)
st.write("Editor Theme:", st.session_state.editor_theme)
st.write("Font Size:", st.session_state.font_size)

# Test project functions
st.subheader("Project Functions")
if st.button("Save Test Project"):
    project_id = save_project("Test Project", "<html><body><h1>Test Project</h1></body></html>", ["Test prompt"])
    st.success(f"Project saved with ID: {project_id}")

if st.button("List Projects"):
    projects = list_projects()
    st.write("Projects:", projects)

# Test API functions
st.subheader("API Functions")
if st.button("Test API Connection"):
    if not st.session_state.api_key:
        st.error("Please enter your OpenRouter API key in the sidebar.")
    else:
        with st.spinner("Testing API connection..."):
            result = generate_html_with_ai("Create a simple HTML page with a heading and a paragraph.", st.session_state.api_key)
            if result:
                st.success("API connection successful!")
                st.code(result, language="html")
            else:
                st.error("API connection failed.")

# Footer
st.markdown("---")
st.markdown("<div class='footer'>DeepSite Test - Testing the application functionality.</div>", unsafe_allow_html=True) 