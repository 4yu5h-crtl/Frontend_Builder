import os
import sys
import json
import requests
from dotenv import load_dotenv

def check_directories():
    """
    Check if all required directories exist.
    
    Returns:
        dict: A dictionary with the status of each directory.
    """
    required_dirs = ["components", "utils", "styles", "projects", "examples"]
    results = {}
    
    for directory in required_dirs:
        exists = os.path.exists(directory)
        results[directory] = {
            "exists": exists,
            "status": "OK" if exists else "Missing"
        }
    
    return results

def check_files():
    """
    Check if all required files exist.
    
    Returns:
        dict: A dictionary with the status of each file.
    """
    required_files = [
        "app.py", 
        "requirements.txt", 
        "README.md", 
        "components/sidebar.py",
        "components/editor.py",
        "components/deployment.py",
        "components/remix.py",
        "components/settings.py",
        "components/projects.py",
        "utils/api.py",
        "utils/deployment.py",
        "utils/editor.py",
        "utils/init.py",
        "utils/monaco.py",
        "utils/project.py",
        "styles/main.css"
    ]
    results = {}
    
    for file in required_files:
        exists = os.path.exists(file)
        results[file] = {
            "exists": exists,
            "status": "OK" if exists else "Missing"
        }
    
    return results

def check_api_key():
    """
    Check if the API key is set.
    
    Returns:
        dict: A dictionary with the status of the API key.
    """
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    
    return {
        "exists": bool(api_key),
        "status": "OK" if api_key else "Missing",
        "length": len(api_key) if api_key else 0
    }

def check_openrouter_api():
    """
    Check if the OpenRouter API is accessible.
    
    Returns:
        dict: A dictionary with the status of the API.
    """
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    
    if not api_key:
        return {
            "accessible": False,
            "status": "API key missing",
            "error": "API key not set"
        }
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(
            "https://openrouter.ai/api/v1/models",
            headers=headers
        )
        
        if response.status_code == 200:
            return {
                "accessible": True,
                "status": "OK",
                "models": len(response.json().get("data", []))
            }
        else:
            return {
                "accessible": False,
                "status": f"Error: {response.status_code}",
                "error": response.text
            }
    except Exception as e:
        return {
            "accessible": False,
            "status": "Error",
            "error": str(e)
        }

def main():
    """
    Run the health check.
    """
    print("Running DeepSite health check...")
    
    # Check directories
    print("\nChecking directories...")
    dir_results = check_directories()
    for directory, result in dir_results.items():
        print(f"  {directory}: {result['status']}")
    
    # Check files
    print("\nChecking files...")
    file_results = check_files()
    for file, result in file_results.items():
        print(f"  {file}: {result['status']}")
    
    # Check API key
    print("\nChecking API key...")
    api_key_result = check_api_key()
    print(f"  API key: {api_key_result['status']}")
    
    # Check OpenRouter API
    print("\nChecking OpenRouter API...")
    api_result = check_openrouter_api()
    print(f"  API accessible: {api_result['accessible']}")
    print(f"  Status: {api_result['status']}")
    if "error" in api_result:
        print(f"  Error: {api_result['error']}")
    
    # Summary
    print("\nSummary:")
    dir_ok = all(result["exists"] for result in dir_results.values())
    file_ok = all(result["exists"] for result in file_results.values())
    api_key_ok = api_key_result["exists"]
    api_ok = api_result["accessible"]
    
    print(f"  Directories: {'OK' if dir_ok else 'Issues found'}")
    print(f"  Files: {'OK' if file_ok else 'Issues found'}")
    print(f"  API key: {'OK' if api_key_ok else 'Missing'}")
    print(f"  OpenRouter API: {'OK' if api_ok else 'Issues found'}")
    
    overall_ok = dir_ok and file_ok and api_key_ok and api_ok
    print(f"\nOverall status: {'OK' if overall_ok else 'Issues found'}")

if __name__ == "__main__":
    main() 