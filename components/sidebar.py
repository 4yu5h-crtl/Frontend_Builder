import streamlit as st
from utils.project import list_projects

def render_sidebar():
    """
    Render the sidebar for the application.
    
    Returns:
        str: The selected page.
    """
    with st.sidebar:
        st.markdown("<h1 class='sidebar-header'>Frontend Developer</h1>", unsafe_allow_html=True)
        st.markdown("Create, edit, and deploy HTML websites with AI assistance.")
        
        # API Key input
        st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
        st.markdown("### API Key")
        api_key = st.text_input("OpenRouter API Key", value=st.session_state.api_key, type="password")
        if api_key != st.session_state.api_key:
            st.session_state.api_key = api_key
            st.success("API key updated!")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Navigation
        st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
        st.markdown("### Navigation")
        page = st.radio("Go to", ["Home", "Settings", "Deploy", "Remix", "Projects"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Projects
        if page == "Projects":
            st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
            st.markdown("### Your Projects")
            projects = list_projects()
            
            if not projects:
                st.info("You don't have any projects yet.")
            else:
                for project in projects:
                    if st.button(f"📁 {project['name']}", key=f"project-{project['id']}"):
                        st.session_state.current_project = project['id']
                        st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        # About
        st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
        st.markdown("### About")
        st.markdown("Frontend Developer is a web application that allows users to create, edit, and deploy HTML websites using AI assistance.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    return page 