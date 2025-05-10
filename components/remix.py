import streamlit as st
from utils.project import load_project

def render_remix():
    """
    Render the remix component.
    """
    st.markdown("<h2 class='sub-header'>Remix Options</h2>", unsafe_allow_html=True)
    
    # Project ID input
    project_id = st.text_input("Project ID")
    
    # Remix button
    if st.button("Load Project"):
        if not project_id:
            st.error("Please enter a project ID.")
        else:
            with st.spinner("Loading project..."):
                # Load the project
                project_name, html_content, prompt_history = load_project(project_id)
                
                if project_name and html_content and prompt_history:
                    st.session_state.html_content = html_content
                    st.session_state.prompt_history = prompt_history
                    st.session_state.current_project = project_id
                    st.success(f"Project '{project_name}' loaded successfully!")
                    st.rerun()
                else:
                    st.error(f"Failed to load project '{project_id}'.") 