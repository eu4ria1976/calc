#!/usr/bin/env python3
"""
Build script for Scientific Calculator Application
Creates a standalone Windows executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        return False
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
        return True
    except ImportError:
        print("Error: PyInstaller is not installed")
        print("Please install it using: pip install pyinstaller")
        return False

def activate_virtual_environment():
    """Activate virtual environment if it exists"""
    venv_path = Path("venv")
    if venv_path.exists():
        print("Virtual environment found, activating...")
        # On Windows, the activation script is in Scripts directory
        activate_script = venv_path / "Scripts" / "activate.bat"
        if not activate_script.exists():
            activate_script = venv_path / "bin" / "activate"
        if activate_script.exists():
            print(f"Found activation script: {activate_script}")
        else:
            print("Activation script not found, proceeding with current environment")
    else:
        print("No virtual environment found, using current environment")

def run_pyinstaller():
    """Run PyInstaller with the spec file"""
    print("Building executable with PyInstaller...")
    
    # Check if spec file exists
    spec_file = "calculator.spec"
    if not os.path.exists(spec_file):
        print(f"Error: Spec file {spec_file} not found")
        return False
    
    # Run PyInstaller command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--clean",
        spec_file
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("PyInstaller build completed successfully")
        if result.stdout:
            print("Output:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("Error during PyInstaller build:")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def post_build_steps():
    """Perform post-build steps"""
    print("Performing post-build steps...")
    
    # Create dist directory if it doesn't exist
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)
    
    # Move executable to dist directory if it's not already there
    exe_name = "ScientificCalculator.exe"
    built_exe = Path(exe_name)
    target_exe = dist_dir / exe_name
    
    if built_exe.exists():
        if not target_exe.exists():
            shutil.move(str(built_exe), str(target_exe))
            print(f"Moved {exe_name} to {dist_dir}/")
        else:
            print(f"Executable already exists in {dist_dir}/")
    
    print(f"Build completed. Executable is located at: {target_exe}")
    return True

def main():
    """Main build function"""
    print("Scientific Calculator Build Script")
    print("=" * 35)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    if not check_dependencies():
        sys.exit(1)
    
    # Activate virtual environment
    activate_virtual_environment()
    
    # Run PyInstaller
    if not run_pyinstaller():
        print("Build failed")
        sys.exit(1)
    
    # Post-build steps
    if not post_build_steps():
        print("Post-build steps failed")
        sys.exit(1)
    
    print("\nBuild completed successfully!")
    print("Executable location: dist/ScientificCalculator.exe")

if __name__ == "__main__":
    main()