import streamlit as st

def render_settings():
    """
    Render the settings component.
    """
    st.markdown("<h2 class='sub-header'>API Key</h2>", unsafe_allow_html=True)
    
    # API Key settings
    api_key = st.text_input("OpenRouter API Key", value=st.session_state.api_key, type="password", key="api_key_input")
    if api_key != st.session_state.api_key:
        st.session_state.api_key = api_key
        st.success("API key updated!")
    
    # Editor settings
    st.markdown("<h2 class='sub-header'>Editor Settings</h2>", unsafe_allow_html=True)
    
    editor_theme = st.selectbox("Editor Theme", ["light", "dark"], index=1 if st.session_state.editor_theme == "vs-dark" else 0, key="editor_theme_select")
    if editor_theme != st.session_state.editor_theme:
        st.session_state.editor_theme = editor_theme
    
    font_size = st.slider("Font Size", 10, 20, st.session_state.font_size, key="font_size_slider")
    if font_size != st.session_state.font_size:
        st.session_state.font_size = font_size
    
    # Save settings
    if st.button("Save Settings", key="save_settings_button"):
        st.success("Settings saved!") 