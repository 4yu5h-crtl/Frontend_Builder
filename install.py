import os
import sys
import subprocess
import platform
import shutil
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

def check_python_version():
    """Check if Python version is compatible."""
    print_step("Checking Python version...")
    
    major, minor = sys.version_info[:2]
    if major < 3 or (major == 3 and minor < 7):
        print_error(f"Python 3.7 or higher is required. You have Python {major}.{minor}.")
        return False
    
    print_success(f"Python version {major}.{minor} is compatible.")
    return True

def create_virtual_environment():
    """Create a virtual environment."""
    print_step("Creating virtual environment...")
    
    venv_dir = "venv"
    if os.path.exists(venv_dir):
        print(f"Virtual environment already exists at {venv_dir}.")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
        print_success(f"Virtual environment created at {venv_dir}.")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to create virtual environment: {e}")
        return False

def install_dependencies():
    """Install dependencies from requirements.txt."""
    print_step("Installing dependencies...")
    
    if not os.path.exists("requirements.txt"):
        print_error("requirements.txt not found.")
        return False
    
    # Determine the pip command based on the platform
    if platform.system() == "Windows":
        pip_cmd = os.path.join("venv", "Scripts", "pip")
    else:
        pip_cmd = os.path.join("venv", "bin", "pip")
    
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print_success("Dependencies installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False

def create_directories():
    """Create required directories if they don't exist."""
    print_step("Creating required directories...")
    
    required_dirs = ["components", "utils", "styles", "projects", "examples"]
    
    for directory in required_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")
    
    print_success("All required directories created.")

def create_env_file():
    """Create .env file if it doesn't exist."""
    print_step("Creating .env file...")
    
    env_file = ".env"
    if os.path.exists(env_file):
        print(f".env file already exists.")
        return True
    
    try:
        with open(env_file, "w") as f:
            f.write("# DeepSite Configuration\n")
            f.write("# Add your OpenRouter API key below\n")
            f.write("OPENROUTER_API_KEY=your_api_key_here\n")
        
        print_success(f".env file created at {env_file}.")
        print("Please edit the .env file to add your OpenRouter API key.")
        return True
    except Exception as e:
        print_error(f"Failed to create .env file: {e}")
        return False

def create_example_project():
    """Create an example project."""
    print_step("Creating example project...")
    
    example_dir = "examples"
    if not os.path.exists(example_dir):
        os.makedirs(example_dir)
    
    example_file = os.path.join(example_dir, "simple_landing_page.html")
    
    try:
        with open(example_file, "w") as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Landing Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background: #35424a;
            color: white;
            padding: 20px 0;
            text-align: center;
        }
        .main-content {
            background: white;
            padding: 20px;
            margin-top: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .cta-button {
            display: inline-block;
            background: #e8491d;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 20px;
            background: #35424a;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Welcome to Our Company</h1>
            <p>We provide the best services for your needs</p>
        </div>
    </header>
    
    <div class="container">
        <div class="main-content">
            <h2>About Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.</p>
            
            <h2>Our Services</h2>
            <p>We offer a wide range of services including:</p>
            <ul>
                <li>Web Design</li>
                <li>Graphic Design</li>
                <li>Digital Marketing</li>
                <li>Content Creation</li>
            </ul>
            
            <a href="#" class="cta-button">Get Started</a>
        </div>
    </div>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 Our Company. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>""")
        
        print_success(f"Example project created at {example_file}.")
        return True
    except Exception as e:
        print_error(f"Failed to create example project: {e}")
        return False

def main():
    """Main installation function."""
    print_header("DeepSite Installation")
    
    # Check Python version
    if not check_python_version():
        print_error("Installation failed due to incompatible Python version.")
        return False
    
    # Create virtual environment
    if not create_virtual_environment():
        print_error("Installation failed due to virtual environment creation error.")
        return False
    
    # Install dependencies
    if not install_dependencies():
        print_error("Installation failed due to dependency installation error.")
        return False
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    # Create example project
    create_example_project()
    
    print_header("Installation Complete")
    print("To run the application, use one of the following commands:")
    print("\n1. Using Python directly:")
    print("   - On Windows: venv\\Scripts\\python app.py")
    print("   - On macOS/Linux: venv/bin/python app.py")
    
    print("\n2. Using Streamlit:")
    print("   - On Windows: venv\\Scripts\\streamlit run app.py")
    print("   - On macOS/Linux: venv/bin/streamlit run app.py")
    
    print("\nDon't forget to edit the .env file to add your OpenRouter API key.")
    
    return True

if __name__ == "__main__":
    main() 