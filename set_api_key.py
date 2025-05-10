import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the API key in the session state
st.session_state.api_key = "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"

# Save the API key to the .env file
with open(".env", "w") as f:
    f.write("# DeepSite Configuration\n")
    f.write("# OpenRouter API Key\n")
    f.write(f"OPENROUTER_API_KEY={st.session_state.api_key}\n")

print("API key has been set in the session state and saved to the .env file.") 