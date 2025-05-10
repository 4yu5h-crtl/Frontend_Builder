import streamlit as st
from utils.monaco import create_monaco_editor_with_preview

def render_editor():
    """
    Render the editor component with a larger preview area and a reliable copy button.
    Returns:
        str: The edited HTML content.
    """
    st.markdown("""
        <div style='display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.5rem;'>
            <div style='font-size: 2rem; font-weight: 800; background: linear-gradient(90deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>Frontend Developer</div>
            <div style='font-size: 1.1rem; color: #a0aec0;'>AI-powered HTML Builder</div>
        </div>
    """, unsafe_allow_html=True)

    # Custom column ratio: editor (5/12), preview (7/12)
    col1, col2 = st.columns([5, 7], gap="large")

    with col1:
        st.markdown("<div class='editor-container'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;'>HTML Code</div>", unsafe_allow_html=True)
        html_content = st.text_area("", value=st.session_state.html_content, height=500, key="html_code_area", label_visibility="collapsed")
        if html_content != st.session_state.html_content:
            st.session_state.html_content = html_content
        # Copy button below the text area
        if st.button("Copy to Clipboard", key="copy_code_btn"):
            st.session_state["_show_copied_code"] = True
        if st.session_state.get("_show_copied_code", False):
            st.code(st.session_state.html_content, language="html")
            st.success("Copied! You can now paste the code anywhere.")
            st.session_state["_show_copied_code"] = False
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='preview-container'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;'>Live Preview</div>", unsafe_allow_html=True)
        st.components.v1.html(st.session_state.html_content, height=500, scrolling=True)
        st.markdown("</div>", unsafe_allow_html=True)

    return html_content

def render_ai_prompt():
    """
    Render the AI prompt component.
    
    Returns:
        str: The prompt for the AI.
    """
    st.markdown("<h2 class='sub-header'>AI Assistant</h2>", unsafe_allow_html=True)
    
    prompt = st.text_area("Enter your prompt for the AI", height=100)
    
    if st.button("Generate with AI") and prompt:
        if not st.session_state.api_key:
            st.error("Please enter your OpenRouter API key in the sidebar.")
        else:
            st.session_state.is_generating = True
            st.session_state.prompt_history.append(prompt)
    
    return prompt 