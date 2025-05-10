import requests
import json
import streamlit as st
import time

def generate_html_with_ai(prompt, api_key):
    """
    Generate HTML content using OpenRouter API.
    
    Args:
        prompt (str): The user's prompt for generating HTML
        api_key (str): The OpenRouter API key
        
    Returns:
        str: The generated HTML content or None if generation failed
    """
    if not api_key:
        st.error("API key is required for AI generation.")
        return None
    
    # Add context to the prompt
    full_prompt = f"""
    You are an expert web developer. Create a complete HTML website based on the following description:
    
    {prompt}
    
    Provide ONLY the HTML code without any explanations or markdown formatting.
    The HTML should be complete and ready to use, including all necessary CSS and JavaScript.
    """
    
    try:
        # Call OpenRouter API
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "x-ai/grok-3-mini-beta",
            "messages": [
                {"role": "system", "content": "You are an expert web developer who specializes in crafting complete, highly functional, and visually stunning frontend interfaces. Your designs follow modern UI/UX principles with a strong focus on responsiveness, minimalism, and aesthetic elegance. You build sleek, interactive, and performance-optimized web applications that integrate smooth animations, motion effects, and dynamic transitions to enhance user experience. Each component you create—whether it's cards, modals, sliders, or interactive sections—is polished, visually engaging, and highly intuitive. You maintain clear typographic hierarchy, consistent spacing, and organized content flow throughout. The goal is to deliver seamless digital experiences with immersive visuals and fluid interactions that work flawlessly across all devices."},
                {"role": "user", "content": full_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 4000
        }
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )
        
        if response.status_code == 200:
            result = response.json()
            generated_content = result["choices"][0]["message"]["content"]
            
            # Extract HTML from the response
            # The model might wrap the HTML in markdown code blocks
            if "```html" in generated_content:
                html_content = generated_content.split("```html")[1].split("```")[0].strip()
            elif "```" in generated_content:
                html_content = generated_content.split("```")[1].split("```")[0].strip()
            else:
                html_content = generated_content.strip()
            
            return html_content
        else:
            st.error(f"API error: {response.status_code} - {response.text}")
            return None
    
    except Exception as e:
        st.error(f"Error generating HTML: {str(e)}")
        return None

def stream_html_with_ai(prompt, api_key):
    """
    Stream HTML content generation using OpenRouter API.
    
    Args:
        prompt (str): The user's prompt for generating HTML
        api_key (str): The OpenRouter API key
        
    Returns:
        generator: A generator that yields chunks of the generated HTML
    """
    if not api_key:
        st.error("API key is required for AI generation.")
        return None
    
    # Add context to the prompt
    full_prompt = f"""
    You are an expert web developer. Create a complete HTML website based on the following description:
    
    {prompt}
    
    Provide ONLY the HTML code without any explanations or markdown formatting.
    The HTML should be complete and ready to use, including all necessary CSS and JavaScript.
    """
    
    try:
        # Call OpenRouter API with streaming
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "x-ai/grok-3-mini-beta",
            "messages": [
                {"role": "system", "content": "You are an expert web developer who creates complete, functional HTML websites."},
                {"role": "user", "content": full_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 4000,
            "stream": True
        }
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data),
            stream=True
        )
        
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]
                        if data == '[DONE]':
                            break
                        try:
                            chunk = json.loads(data)
                            if 'choices' in chunk and len(chunk['choices']) > 0:
                                delta = chunk['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    yield delta['content']
                        except json.JSONDecodeError:
                            continue
        else:
            st.error(f"API error: {response.status_code} - {response.text}")
            return None
    
    except Exception as e:
        st.error(f"Error generating HTML: {str(e)}")
        return None 