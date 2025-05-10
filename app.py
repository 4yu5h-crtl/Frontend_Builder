import streamlit as st
import os
from dotenv import load_dotenv
import time

# Import utility functions
from utils.init import init_session_state, load_custom_css, setup_page_config
from utils.api import generate_html_with_ai, stream_html_with_ai

# Import components
from components.sidebar import render_sidebar
from components.editor import render_editor, render_ai_prompt
from components.deployment import render_deployment
from components.remix import render_remix
from components.settings import render_settings
from components.projects import render_projects

# Initialize the application
setup_page_config()
init_session_state()
load_custom_css()

# Render the sidebar
page = render_sidebar()

# Main content
if page == "Home":
    st.markdown("<h1 class='main-header'>Frontend Developer Editor</h1>", unsafe_allow_html=True)
    
    # Render the editor
    html_content = render_editor()
    
    # Render the AI prompt
    prompt = render_ai_prompt()
    
    # Handle AI generation
    if st.session_state.is_generating and prompt:
        with st.spinner("Generating HTML with AI..."):
            # Generate HTML with AI
            generated_html = generate_html_with_ai(prompt, st.session_state.api_key)
            
            if generated_html:
                st.session_state.html_content = generated_html
                st.session_state.is_generating = False
                st.success("HTML generated successfully!")
                st.rerun()
            else:
                st.error("Failed to generate HTML with AI. Please check your API key and try again.")
                st.session_state.is_generating = False

elif page == "Settings":
    st.markdown("<h1 class='main-header'>Settings</h1>", unsafe_allow_html=True)
    
    # Render the settings
    render_settings()

elif page == "Deploy":
    st.markdown("<h1 class='main-header'>Deploy</h1>", unsafe_allow_html=True)
    
    # Render the deployment
    render_deployment()

elif page == "Remix":
    st.markdown("<h1 class='main-header'>Remix</h1>", unsafe_allow_html=True)
    
    # Render the remix
    render_remix()

elif page == "Projects":
    st.markdown("<h1 class='main-header'>Projects</h1>", unsafe_allow_html=True)
    
    # Render the projects
    render_projects()

# Footer
st.markdown("---")
st.markdown("<div class='footer'>Frontend Developer - Create, edit, and deploy HTML websites with AI assistance.</div>", unsafe_allow_html=True) 