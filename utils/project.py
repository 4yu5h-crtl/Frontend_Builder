import os
import json
import uuid
import datetime
import streamlit as st

# Define the projects directory
PROJECTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "projects")

# Ensure the projects directory exists
os.makedirs(PROJECTS_DIR, exist_ok=True)

def save_project(project_name, html_content, prompt_history=None):
    """
    Save a project to the projects directory.
    
    Args:
        project_name (str): The name of the project
        html_content (str): The HTML content of the project
        prompt_history (list, optional): The history of prompts used to generate the project
        
    Returns:
        str: The project ID
    """
    # Generate a unique project ID
    project_id = str(uuid.uuid4())
    
    # Create project data
    project_data = {
        "id": project_id,
        "name": project_name,
        "html_content": html_content,
        "prompt_history": prompt_history or [],
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat()
    }
    
    # Save project to file
    project_file = os.path.join(PROJECTS_DIR, f"{project_id}.json")
    with open(project_file, "w") as f:
        json.dump(project_data, f, indent=2)
    
    return project_id

def load_project(project_id):
    """
    Load a project from the projects directory.
    
    Args:
        project_id (str): The ID of the project to load
        
    Returns:
        dict: The project data or None if the project doesn't exist
    """
    project_file = os.path.join(PROJECTS_DIR, f"{project_id}.json")
    
    if not os.path.exists(project_file):
        return None
    
    with open(project_file, "r") as f:
        project_data = json.load(f)
    
    return project_data

def delete_project(project_id):
    """
    Delete a project from the projects directory.
    
    Args:
        project_id (str): The ID of the project to delete
        
    Returns:
        bool: True if the project was deleted, False otherwise
    """
    project_file = os.path.join(PROJECTS_DIR, f"{project_id}.json")
    
    if not os.path.exists(project_file):
        return False
    
    os.remove(project_file)
    return True

def list_projects():
    """
    List all projects in the projects directory.
    
    Returns:
        list: A list of project data dictionaries
    """
    projects = []
    
    for filename in os.listdir(PROJECTS_DIR):
        if filename.endswith(".json"):
            project_file = os.path.join(PROJECTS_DIR, filename)
            with open(project_file, "r") as f:
                project_data = json.load(f)
                projects.append(project_data)
    
    # Sort projects by updated_at date (newest first)
    projects.sort(key=lambda x: x["updated_at"], reverse=True)
    
    return projects

def update_project(project_id, html_content=None, prompt_history=None):
    """
    Update a project in the projects directory.
    
    Args:
        project_id (str): The ID of the project to update
        html_content (str, optional): The new HTML content
        prompt_history (list, optional): The new prompt history
        
    Returns:
        bool: True if the project was updated, False otherwise
    """
    project_file = os.path.join(PROJECTS_DIR, f"{project_id}.json")
    
    if not os.path.exists(project_file):
        return False
    
    with open(project_file, "r") as f:
        project_data = json.load(f)
    
    if html_content is not None:
        project_data["html_content"] = html_content
    
    if prompt_history is not None:
        project_data["prompt_history"] = prompt_history
    
    project_data["updated_at"] = datetime.datetime.now().isoformat()
    
    with open(project_file, "w") as f:
        json.dump(project_data, f, indent=2)
    
    return True 