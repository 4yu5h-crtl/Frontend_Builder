import os
import sys
import subprocess
import platform
import argparse
from pathlib import Path

def print_header(message):
    """Print a formatted header message."""
    print("\n" + "=" * 80)
    print(f" {message} ".center(80, "="))
    print("=" * 80 + "\n")

def print_step(message):
    """Print a formatted step message."""
    print(f"\n>>> {message}")

def print_success(message):
    """Print a formatted success message."""
    print(f"\n✓ {message}")

def print_error(message):
    """Print a formatted error message."""
    print(f"\n✗ {message}")

def check_venv():
    """Check if virtual environment exists."""
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        print_error(f"Virtual environment not found at {venv_dir}.")
        print("Please run 'python install.py' first to set up the environment.")
        return False
    
    return True

def check_env_file():
    """Check if .env file exists and has API key."""
    env_file = ".env"
    if not os.path.exists(env_file):
        print_error(f".env file not found.")
        print("Please run 'python install.py' first to set up the environment.")
        return False
    
    # Check if API key is set
    with open(env_file, "r") as f:
        content = f.read()
        if "OPENROUTER_API_KEY=your_api_key_here" in content or "OPENROUTER_API_KEY=" in content:
            print_error("OpenRouter API key not set in .env file.")
            print("Please edit the .env file to add your OpenRouter API key.")
            return False
    
    return True

def run_app(use_streamlit=True, port=8501):
    """Run the application."""
    print_step("Starting DeepSite...")
    
    # Determine the Python command based on the platform
    if platform.system() == "Windows":
        python_cmd = os.path.join("venv", "Scripts", "python")
        streamlit_cmd = os.path.join("venv", "Scripts", "streamlit")
    else:
        python_cmd = os.path.join("venv", "bin", "python")
        streamlit_cmd = os.path.join("venv", "bin", "streamlit")
    
    try:
        if use_streamlit:
            print(f"Running with Streamlit on port {port}...")
            subprocess.run([streamlit_cmd, "run", "app.py", "--server.port", str(port)], check=True)
        else:
            print("Running with Python directly...")
            subprocess.run([python_cmd, "app.py"], check=True)
        
        print_success("Application stopped.")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to run application: {e}")
        return False
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
        return True

def main():
    """Main function to run the application."""
    parser = argparse.ArgumentParser(description="Run the DeepSite application.")
    parser.add_argument("--no-streamlit", action="store_true", help="Run without Streamlit (direct Python execution)")
    parser.add_argument("--port", type=int, default=8501, help="Port to run Streamlit on (default: 8501)")
    
    args = parser.parse_args()
    
    print_header("DeepSite Launcher")
    
    # Check if virtual environment exists
    if not check_venv():
        return False
    
    # Check if .env file exists and has API key
    if not check_env_file():
        return False
    
    # Run the application
    run_app(not args.no_streamlit, args.port)
    
    return True

if __name__ == "__main__":
    main() 