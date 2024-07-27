import subprocess
import sys
import os

def check_pip():
    """Check if pip is installed."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_pip():
    """Install pip."""
    try:
        subprocess.run([sys.executable, "-m", "ensurepip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pip: {e}")
        return False

def move_pip_to_admin_path():
    """Move pip to admin path."""
    try:
        pip_path = subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, stdout=subprocess.PIPE).stdout.decode()
        pip_dir = os.path.dirname(pip_path.split()[3])
        os.environ["PATH"] += os.pathsep + pip_dir
    except Exception as e:
        print(f"Failed to move pip to admin path: {e}")

def install_requirements():
    """Install packages from requirements.txt."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")

def main():
    if not check_pip():
        print("Pip not found. Installing pip...")
        if install_pip():
            move_pip_to_admin_path()
        else:
            sys.exit(1)

    print("Installing requirements from requirements.txt...")
    install_requirements()

    # Run the main.py script
    script_path = os.path.join(os.path.dirname(__file__), 'unlimited.py')
    if os.path.exists(script_path):
        subprocess.run([sys.executable, script_path], check=True)
    else:
        print(f"main.py not found at {script_path}")

if __name__ == "__main__":
    main()
