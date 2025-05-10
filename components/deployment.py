import streamlit as st
from utils.deployment import (
    deploy_to_github_pages,
    deploy_to_netlify,
    deploy_to_vercel,
    save_project_locally
)
from utils.project import save_project

def render_deployment():
    """
    Render the deployment component.
    """
    st.markdown("<h2 class='sub-header'>Deployment Options</h2>", unsafe_allow_html=True)
    
    # Deployment platform
    deployment_platform = st.selectbox("Deployment Platform", ["GitHub Pages", "Netlify", "Vercel", "Local"])
    
    # Project name
    project_name = st.text_input("Project Name", "my-deepsite-project")
    
    # Deployment options based on platform
    if deployment_platform == "GitHub Pages":
        github_token = st.text_input("GitHub Personal Access Token", type="password")
        repo_name = st.text_input("Repository Name", project_name.lower().replace(" ", "-"))
        
        if st.button("Deploy to GitHub Pages"):
            if not project_name:
                st.error("Please enter a project name.")
            elif not github_token:
                st.error("Please enter your GitHub personal access token.")
            else:
                with st.spinner("Deploying to GitHub Pages..."):
                    success = deploy_to_github_pages(
                        project_name,
                        st.session_state.html_content,
                        st.session_state.prompt_history,
                        github_token,
                        repo_name
                    )
                    
                    if success:
                        # Save the project locally
                        project_id = save_project(project_name, st.session_state.html_content, st.session_state.prompt_history)
                        st.session_state.current_project = project_id
                        st.success(f"Project '{project_name}' deployed successfully to GitHub Pages!")
    
    elif deployment_platform == "Netlify":
        netlify_token = st.text_input("Netlify Personal Access Token", type="password")
        site_name = st.text_input("Site Name", project_name.lower().replace(" ", "-"))
        
        if st.button("Deploy to Netlify"):
            if not project_name:
                st.error("Please enter a project name.")
            elif not netlify_token:
                st.error("Please enter your Netlify personal access token.")
            else:
                with st.spinner("Deploying to Netlify..."):
                    success = deploy_to_netlify(
                        project_name,
                        st.session_state.html_content,
                        st.session_state.prompt_history,
                        netlify_token,
                        site_name
                    )
                    
                    if success:
                        # Save the project locally
                        project_id = save_project(project_name, st.session_state.html_content, st.session_state.prompt_history)
                        st.session_state.current_project = project_id
                        st.success(f"Project '{project_name}' deployed successfully to Netlify!")
    
    elif deployment_platform == "Vercel":
        vercel_token = st.text_input("Vercel Personal Access Token", type="password")
        project_id = st.text_input("Project ID (leave empty to create a new project)")
        
        if st.button("Deploy to Vercel"):
            if not project_name:
                st.error("Please enter a project name.")
            elif not vercel_token:
                st.error("Please enter your Vercel personal access token.")
            else:
                with st.spinner("Deploying to Vercel..."):
                    success = deploy_to_vercel(
                        project_name,
                        st.session_state.html_content,
                        st.session_state.prompt_history,
                        vercel_token,
                        project_id
                    )
                    
                    if success:
                        # Save the project locally
                        project_id = save_project(project_name, st.session_state.html_content, st.session_state.prompt_history)
                        st.session_state.current_project = project_id
                        st.success(f"Project '{project_name}' deployed successfully to Vercel!")
    
    elif deployment_platform == "Local":
        if st.button("Save Project Locally"):
            if not project_name:
                st.error("Please enter a project name.")
            else:
                with st.spinner("Saving project locally..."):
                    # Save the project locally
                    project_id = save_project(project_name, st.session_state.html_content, st.session_state.prompt_history)
                    st.session_state.current_project = project_id
                    st.success(f"Project '{project_name}' saved successfully!") 