import streamlit as st
from utils.project import list_projects, load_project, delete_project

def render_projects():
    """
    Render the projects component.
    """
    st.markdown("<h2 class='sub-header'>Your Projects</h2>", unsafe_allow_html=True)
    
    # Get all projects
    projects = list_projects()
    
    if not projects:
        st.info("You don't have any projects yet.")
    else:
        # Display projects in a table
        st.markdown("<table class='projects-table'>", unsafe_allow_html=True)
        st.markdown("<tr><th>Name</th><th>Created</th><th>Actions</th></tr>", unsafe_allow_html=True)
        
        for project in projects:
            st.markdown(f"<tr>", unsafe_allow_html=True)
            st.markdown(f"<td>{project['name']}</td>", unsafe_allow_html=True)
            st.markdown(f"<td>{project['created_at']}</td>", unsafe_allow_html=True)
            st.markdown(f"<td>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Load", key=f"load-{project['id']}"):
                    project_name, html_content, prompt_history = load_project(project['id'])
                    
                    if project_name and html_content and prompt_history:
                        st.session_state.html_content = html_content
                        st.session_state.prompt_history = prompt_history
                        st.session_state.current_project = project['id']
                        st.success(f"Project '{project_name}' loaded successfully!")
                        st.rerun()
            
            with col2:
                if st.button("Delete", key=f"delete-{project['id']}"):
                    if delete_project(project['id']):
                        st.success(f"Project '{project['name']}' deleted successfully!")
                        st.rerun()
            
            st.markdown(f"</td>", unsafe_allow_html=True)
            st.markdown(f"</tr>", unsafe_allow_html=True)
        
        st.markdown("</table>", unsafe_allow_html=True) 