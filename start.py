#!/usr/bin/env python3
# BillKaro Startup Script

import subprocess
import sys
import os

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False
    return True

def start_application():
    try:
        os.system("python app.py")
    except KeyboardInterrupt:
        print("\nApplication stopped.")

if __name__ == "__main__":
    print("BillKaro - Bank Statement Converter")
    print("=" * 40)
    
    # Check if requirements are installed
    if not os.path.exists("requirements.txt"):
        print("Requirements file not found!")
        sys.exit(1)
    
    # Install dependencies
    print("Installing dependencies...")
    if install_requirements():
        print("\nStarting BillKaro application...")
        print("Open your browser and go to: http://localhost:5000")
        print("Press Ctrl+C to stop the application")
        print("-" * 40)
        start_application()
    else:
        print("Failed to install dependencies. Please install manually:")
        print("pip install -r requirements.txt")
