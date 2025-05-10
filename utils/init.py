import streamlit as st
import os
from dotenv import load_dotenv

def init_session_state():
    """
    Initialize the session state variables.
    """
    # Load environment variables
    load_dotenv()
    
    # API Key
    if "api_key" not in st.session_state:
        # Set the API key directly
        st.session_state.api_key = "your-api-key"
    
    # HTML Content
    if "html_content" not in st.session_state:
        st.session_state.html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>AI Assistant</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: linear-gradient(to right, #f0f0f0, #dcdcdc);
      height: 100dvh;
      display: grid;
      place-items: center;
      font-family: 'Segoe UI', sans-serif;
      color: #333;
    }

    .container {
      text-align: center;
      animation: fadeIn 1.5s ease-out;
    }

    h1 {
      font-size: 42px;
      margin-bottom: 10px;
    }

    h1 span {
      font-weight: normal;
      font-size: 24px;
      color: #777;
    }

    .arrow-down {
      margin-top: 40px;
      width: 40px;
      animation: bounce 2s infinite;
    }

    @keyframes bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(10px); }
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>
      <span>Grok is listening...</span><br/>
      What do you want to develop?
    </h1>
  </div>
</body>
</html>
"""
    
    # Prompt History
    if "prompt_history" not in st.session_state:
        st.session_state.prompt_history = []
    
    # Is Generating
    if "is_generating" not in st.session_state:
        st.session_state.is_generating = False
    
    # Current Project
    if "current_project" not in st.session_state:
        st.session_state.current_project = None
    
    # Editor Settings
    if "editor_theme" not in st.session_state:
        st.session_state.editor_theme = "vs-dark"
    
    if "font_size" not in st.session_state:
        st.session_state.font_size = 14

def load_custom_css():
    """
    Load the custom CSS for the application.
    """
    css_file = os.path.join(os.getcwd(), "styles", "main.css")
    
    if os.path.exists(css_file):
        with open(css_file, "r", encoding="utf-8") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        # Fallback to inline CSS
        st.markdown("""
        <style>
            .main-header {
                font-size: 2.5rem;
                color: #2c3e50;
                margin-bottom: 1rem;
            }
            .sub-header {
                font-size: 1.5rem;
                color: #34495e;
                margin-bottom: 1rem;
            }
            .stButton button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #2980b9;
            }
            .editor-container {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 1rem;
                margin-bottom: 1rem;
            }
            .preview-container {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 1rem;
                margin-bottom: 1rem;
            }
        </style>
        """, unsafe_allow_html=True)

def setup_page_config():
    """
    Set up the page configuration for the application.
    """
    st.set_page_config(
        page_title="Frontend Developer",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="expanded"
    ) 
