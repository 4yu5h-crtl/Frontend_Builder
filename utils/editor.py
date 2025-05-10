import streamlit as st
import streamlit_monaco as st_monaco

def create_monaco_editor(content, language="html", theme="vs-dark", height=500):
    """
    Create a Monaco Editor component.
    
    Args:
        content (str): The initial content of the editor.
        language (str): The language of the content. Defaults to "html".
        theme (str): The theme of the editor. Defaults to "vs-dark".
        height (int): The height of the editor in pixels. Defaults to 500.
        
    Returns:
        str: The content of the editor.
    """
    # This is a placeholder for the actual Monaco Editor integration
    # In a real implementation, this would use the streamlit-monaco package
    
    # For now, we'll just use a text area
    edited_content = st.text_area("Edit your HTML", value=content, height=height)
    
    return edited_content

def create_monaco_editor_with_preview(content, language="html", theme="vs-dark", height=500):
    """
    Create a Monaco Editor component with a preview.
    
    Args:
        content (str): The initial content of the editor.
        language (str): The language of the content. Defaults to "html".
        theme (str): The theme of the editor. Defaults to "vs-dark".
        height (int): The height of the editor in pixels. Defaults to 500.
        
    Returns:
        str: The content of the editor.
    """
    # Create two columns for editor and preview
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h2 class='sub-header'>HTML Editor</h2>", unsafe_allow_html=True)
        edited_content = create_monaco_editor(content, language, theme, height)
    
    with col2:
        st.markdown("<h2 class='sub-header'>Preview</h2>", unsafe_allow_html=True)
        st.components.v1.html(edited_content, height=height, scrolling=True)
    
    return edited_content 