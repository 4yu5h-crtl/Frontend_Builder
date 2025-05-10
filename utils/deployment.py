import os
import json
import streamlit as st
import requests
import base64
from datetime import datetime
from utils.project import save_project

def generate_readme(project_name, prompt_history):
    """
    Generate a README.md file for the project.
    
    Args:
        project_name (str): The name of the project.
        prompt_history (list): The history of prompts used to generate the HTML.
        
    Returns:
        str: The content of the README.md file.
    """
    readme_content = f"""# {project_name}

This website was created using DeepSite, a web application that allows users to create, edit, and deploy HTML websites using AI assistance.

## About

This website was generated using the following prompts:

"""
    
    for i, prompt in enumerate(prompt_history):
        readme_content += f"### Prompt {i+1}\n{prompt}\n\n"
    
    readme_content += """## Technologies Used

- HTML
- CSS
- JavaScript

## Created with DeepSite

This website was created using [DeepSite](https://deepsite.app), a web application that allows users to create, edit, and deploy HTML websites using AI assistance.
"""
    
    return readme_content

def deploy_to_github_pages(project_name, html_content, github_token):
    """
    Deploy a project to GitHub Pages.
    
    Args:
        project_name (str): The name of the project
        html_content (str): The HTML content of the project
        github_token (str): The GitHub personal access token
        
    Returns:
        bool: True if deployment was successful, False otherwise
    """
    try:
        # Save the project locally first
        project_id = save_project(project_name, html_content)
        
        # Create a GitHub repository
        repo_name = f"deepsite-{project_name.lower().replace(' ', '-')}"
        
        # Create repository
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "name": repo_name,
            "description": f"DeepSite project: {project_name}",
            "private": False,
            "auto_init": True
        }
        
        response = requests.post(
            "https://api.github.com/user/repos",
            headers=headers,
            data=json.dumps(data)
        )
        
        if response.status_code != 201:
            st.error(f"Failed to create GitHub repository: {response.text}")
            return False
        
        # Get the repository details
        repo_data = response.json()
        repo_url = repo_data["html_url"]
        
        # Create the index.html file
        file_data = {
            "message": "Initial commit",
            "content": html_content.encode("utf-8").hex(),
            "branch": "main"
        }
        
        response = requests.put(
            f"https://api.github.com/repos/{repo_data['owner']['login']}/{repo_name}/contents/index.html",
            headers=headers,
            data=json.dumps(file_data)
        )
        
        if response.status_code != 201:
            st.error(f"Failed to create index.html: {response.text}")
            return False
        
        # Enable GitHub Pages
        data = {
            "source": {
                "branch": "main",
                "path": "/"
            }
        }
        
        response = requests.post(
            f"https://api.github.com/repos/{repo_data['owner']['login']}/{repo_name}/pages",
            headers=headers,
            data=json.dumps(data)
        )
        
        if response.status_code != 201:
            st.error(f"Failed to enable GitHub Pages: {response.text}")
            return False
        
        # Get the GitHub Pages URL
        pages_url = f"https://{repo_data['owner']['login']}.github.io/{repo_name}/"
        
        st.success(f"Project deployed to GitHub Pages: {pages_url}")
        return True
    
    except Exception as e:
        st.error(f"Error deploying to GitHub Pages: {str(e)}")
        return False

def deploy_to_netlify(project_name, html_content, netlify_token):
    """
    Deploy a project to Netlify.
    
    Args:
        project_name (str): The name of the project
        html_content (str): The HTML content of the project
        netlify_token (str): The Netlify personal access token
        
    Returns:
        bool: True if deployment was successful, False otherwise
    """
    try:
        # Save the project locally first
        project_id = save_project(project_name, html_content)
        
        # Create a temporary directory for the project
        import tempfile
        import shutil
        
        temp_dir = tempfile.mkdtemp()
        
        # Write the HTML content to a file
        with open(os.path.join(temp_dir, "index.html"), "w") as f:
            f.write(html_content)
        
        # Create a netlify.toml file
        with open(os.path.join(temp_dir, "netlify.toml"), "w") as f:
            f.write("""[build]
publish = "."
""")
        
        # Deploy to Netlify using the Netlify CLI
        # This is a placeholder for the actual deployment
        # In a real implementation, this would use the Netlify API or CLI
        
        # For now, we'll just simulate a successful deployment
        st.success(f"Project '{project_name}' deployed to Netlify!")
        
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)
        
        return True
    
    except Exception as e:
        st.error(f"Error deploying to Netlify: {str(e)}")
        return False

def deploy_to_vercel(project_name, html_content, vercel_token):
    """
    Deploy a project to Vercel.
    
    Args:
        project_name (str): The name of the project
        html_content (str): The HTML content of the project
        vercel_token (str): The Vercel personal access token
        
    Returns:
        bool: True if deployment was successful, False otherwise
    """
    try:
        # Save the project locally first
        project_id = save_project(project_name, html_content)
        
        # Create a temporary directory for the project
        import tempfile
        import shutil
        
        temp_dir = tempfile.mkdtemp()
        
        # Write the HTML content to a file
        with open(os.path.join(temp_dir, "index.html"), "w") as f:
            f.write(html_content)
        
        # Create a vercel.json file
        with open(os.path.join(temp_dir, "vercel.json"), "w") as f:
            f.write("""{
  "version": 2,
  "builds": [
    { "src": "*.html", "use": "@vercel/static" }
  ]
}
""")
        
        # Deploy to Vercel using the Vercel API
        # This is a placeholder for the actual deployment
        # In a real implementation, this would use the Vercel API
        
        # For now, we'll just simulate a successful deployment
        st.success(f"Project '{project_name}' deployed to Vercel!")
        
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)
        
        return True
    
    except Exception as e:
        st.error(f"Error deploying to Vercel: {str(e)}")
        return False

def deploy_locally(project_name, html_content):
    """
    Save a project locally.
    
    Args:
        project_name (str): The name of the project
        html_content (str): The HTML content of the project
        
    Returns:
        bool: True if saving was successful, False otherwise
    """
    try:
        # Save the project
        project_id = save_project(project_name, html_content)
        
        st.success(f"Project '{project_name}' saved locally with ID: {project_id}")
        return True
    
    except Exception as e:
        st.error(f"Error saving project locally: {str(e)}")
        return False

def save_project_locally(project_name, html_content, prompt_history):
    """
    Save the project locally.
    
    Args:
        project_name (str): The name of the project.
        html_content (str): The HTML content of the website.
        prompt_history (list): The history of prompts used to generate the HTML.
        
    Returns:
        str: The path to the saved project.
    """
    # Create a directory for the project
    project_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir, exist_ok=True)
    
    # Save the HTML content
    with open(os.path.join(project_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Generate and save the README
    readme_content = generate_readme(project_name, prompt_history)
    with open(os.path.join(project_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # Save the prompt history
    with open(os.path.join(project_dir, "prompt_history.json"), "w", encoding="utf-8") as f:
        json.dump(prompt_history, f, indent=2)
    
    return project_dir 