#!/usr/bin/env python3
"""
Complete Setup Script for GCC Emissions Calculator
Run this after the initial project setup to complete everything
"""

import subprocess
import os
import sys
import time
import webbrowser
import json
from pathlib import Path


def run_command(command, description, shell=True):
    """Run a command and print the result."""
    print(f"\n{'=' * 60}")
    print(f"🔧 {description}")
    print(f"{'=' * 60}")

    try:
        if shell and isinstance(command, list):
            command = ' '.join(command)

        result = subprocess.run(command, shell=shell, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Success: {description}")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ Failed: {description}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            if result.stdout:
                print(f"Output: {result.stdout}")

        return result.returncode == 0
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False


def setup_git():
    """Initialize Git repository."""
    if os.path.exists('.git'):
        print("✅ Git already initialized")
        return True

    return run_command("git init", "Initializing Git repository")


def configure_git():
    """Configure Git with user info if not set."""
    # Check if git config is set
    check_name = subprocess.run("git config user.name", shell=True, capture_output=True, text=True)
    check_email = subprocess.run("git config user.email", shell=True, capture_output=True, text=True)

    if not check_name.stdout.strip():
        run_command('git config user.name "Your Name"', "Setting Git username")
        print("⚠️  Please update git config user.name with your actual name")

    if not check_email.stdout.strip():
        run_command('git config user.email "your.email@example.com"', "Setting Git email")
        print("⚠️  Please update git config user.email with your actual email")


def initial_commit():
    """Make initial commit."""
    # Check if there are any commits
    check_commits = subprocess.run("git log --oneline -1", shell=True, capture_output=True, text=True)

    if check_commits.returncode == 0:
        print("✅ Repository already has commits")
        return True

    run_command("git add .", "Adding all files to Git")
    return run_command('git commit -m "Initial commit - GCC Emissions Calculator for UAE & KSA"',
                       "Making initial commit")


def install_dependencies():
    """Install Python dependencies."""
    print("\n" + "=" * 60)
    print("📦 Installing Dependencies")
    print("=" * 60)

    # Upgrade pip first
    run_command([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], "Upgrading pip")

    # Install requirements
    if os.path.exists("requirements.txt"):
        return run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                           "Installing requirements")
    else:
        print("❌ requirements.txt not found!")
        return False


def run_tests():
    """Run pytest tests."""
    print("\n" + "=" * 60)
    print("🧪 Running Tests")
    print("=" * 60)

    # Check if pytest is installed
    try:
        import pytest
        # Run pytest
        return run_command([sys.executable, "-m", "pytest", "tests/", "-v"], "Running tests")
    except ImportError:
        print("❌ pytest not installed. Installing now...")
        run_command([sys.executable, "-m", "pip", "install", "pytest", "pytest-cov"], "Installing pytest")
        return run_command([sys.executable, "-m", "pytest", "tests/", "-v"], "Running tests")


def create_github_cli_config():
    """Create GitHub CLI configuration script."""
    gh_script = """#!/bin/bash
# GitHub Setup Script
# Run this to create and configure your GitHub repository

REPO_NAME="gcc-emissions-calculator"
REPO_DESCRIPTION="Greenhouse Gas Emissions Calculator for GCC countries (UAE & Saudi Arabia)"

echo "🌍 Setting up GitHub repository: $REPO_NAME"
echo "==========================================="

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Install it from: https://cli.github.com/"
    echo "Or run: winget install --id GitHub.cli"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "🔐 Please authenticate with GitHub:"
    gh auth login
fi

# Create repository
echo "📦 Creating repository..."
gh repo create $REPO_NAME --private --description "$REPO_DESCRIPTION" --source=. --remote=origin --push

echo "✅ Repository created!"
echo "🔗 URL: https://github.com/$(gh api user --jq .login)/$REPO_NAME"

# Enable GitHub Pages
echo "🌐 Enabling GitHub Pages..."
gh api repos/$(gh api user --jq .login)/$REPO_NAME/pages \
  --method POST \
  --field source='{"branch":"main","path":"/docs"}' \
  2>/dev/null || echo "Pages might already be enabled or need manual setup"

echo ""
echo "📋 Next steps:"
echo "1. Go to: https://github.com/$(gh api user --jq .login)/$REPO_NAME/settings/pages"
echo "2. Verify Pages is enabled from main branch /docs folder"
echo "3. Your site will be at: https://$(gh api user --jq .login).github.io/$REPO_NAME/"
echo ""
echo "To make repository public later:"
echo "gh repo edit $REPO_NAME --visibility public"
"""

    with open("setup_github.sh", "w") as f:
        f.write(gh_script)

    # For Windows, create a .bat version too
    bat_script = """@echo off
REM GitHub Setup Script for Windows
REM Run this to create and configure your GitHub repository

set REPO_NAME=gcc-emissions-calculator
set REPO_DESCRIPTION=Greenhouse Gas Emissions Calculator for GCC countries (UAE and Saudi Arabia)

echo Setting up GitHub repository: %REPO_NAME%
echo ===========================================

REM Check if gh is installed
where gh >nul 2>&1
if %errorlevel% neq 0 (
    echo GitHub CLI (gh) is not installed.
    echo Install it from: https://cli.github.com/
    echo Or run: winget install --id GitHub.cli
    exit /b 1
)

REM Check if authenticated
gh auth status >nul 2>&1
if %errorlevel% neq 0 (
    echo Please authenticate with GitHub:
    gh auth login
)

REM Create repository
echo Creating repository...
gh repo create %REPO_NAME% --private --description "%REPO_DESCRIPTION%" --source=. --remote=origin --push

echo Repository created!
for /f "tokens=*" %%a in ('gh api user --jq .login') do set USERNAME=%%a
echo URL: https://github.com/%USERNAME%/%REPO_NAME%

REM Enable GitHub Pages
echo Enabling GitHub Pages...
gh api repos/%USERNAME%/%REPO_NAME%/pages --method POST --field source="{\"branch\":\"main\",\"path\":\"/docs\"}" 2>nul || echo Pages might already be enabled or need manual setup

echo.
echo Next steps:
echo 1. Go to: https://github.com/%USERNAME%/%REPO_NAME%/settings/pages
echo 2. Verify Pages is enabled from main branch /docs folder
echo 3. Your site will be at: https://%USERNAME%.github.io/%REPO_NAME%/
echo.
echo To make repository public later:
echo gh repo edit %REPO_NAME% --visibility public
"""

    with open("setup_github.bat", "w") as f:
        f.write(bat_script)

    print("✅ Created GitHub setup scripts: setup_github.sh and setup_github.bat")
    return True


def create_run_configurations():
    """Create PyCharm run configurations."""
    run_configs_dir = Path(".idea/runConfigurations")
    run_configs_dir.mkdir(parents=True, exist_ok=True)

    # API run configuration
    api_config = """<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Run API" type="PythonConfigurationType" factoryName="Python">
    <module name="gcc-emissions-calculator" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <envs>
      <env name="PYTHONUNBUFFERED" value="1" />
    </envs>
    <option name="SDK_HOME" value="" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <option name="IS_MODULE_SDK" value="true" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <option name="SCRIPT_NAME" value="$PROJECT_DIR$/src/api/app.py" />
    <option name="PARAMETERS" value="" />
    <option name="SHOW_COMMAND_LINE" value="false" />
    <option name="EMULATE_TERMINAL" value="false" />
    <option name="MODULE_MODE" value="false" />
    <option name="REDIRECT_INPUT" value="false" />
    <option name="INPUT_FILE" value="" />
    <method v="2" />
  </configuration>
</component>"""

    with open(run_configs_dir / "Run_API.xml", "w") as f:
        f.write(api_config)

    # Tests run configuration
    tests_config = """<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Run Tests" type="tests" factoryName="py.test">
    <module name="gcc-emissions-calculator" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <option name="SDK_HOME" value="" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <option name="IS_MODULE_SDK" value="true" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <option name="_new_keywords" value="&quot;&quot;" />
    <option name="_new_parameters" value="&quot;&quot;" />
    <option name="_new_additionalArguments" value="&quot;-v&quot;" />
    <option name="_new_target" value="&quot;tests&quot;" />
    <option name="_new_targetType" value="&quot;PATH&quot;" />
    <method v="2" />
  </configuration>
</component>"""

    with open(run_configs_dir / "Run_Tests.xml", "w") as f:
        f.write(tests_config)

    print("✅ Created PyCharm run configurations")
    return True


def open_in_browser():
    """Open the local HTML file in browser."""
    html_path = Path("docs/index.html").absolute()
    if html_path.exists():
        webbrowser.open(f"file://{html_path}")
        print(f"✅ Opened {html_path} in browser")
    else:
        print("❌ docs/index.html not found!")


def create_quick_scripts():
    """Create quick utility scripts."""

    # Create a run_all.py script
    run_all_script = """#!/usr/bin/env python3
# Quick script to run all common tasks

import subprocess
import sys

print("🚀 Running all common tasks...")

# Install dependencies
print("\\n📦 Installing dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run tests
print("\\n🧪 Running tests...")
subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"])

# Start API
print("\\n🌐 Starting API server...")
print("API will be available at: http://localhost:8000")
print("Press Ctrl+C to stop")
subprocess.run([sys.executable, "-m", "src.api.app"])
"""

    with open("run_all.py", "w") as f:
        f.write(run_all_script)

    print("✅ Created run_all.py quick script")


def print_final_instructions():
    """Print final setup instructions."""
    print("\n" + "=" * 60)
    print("✅ SETUP COMPLETE!")
    print("=" * 60)

    print("\n📋 What was done:")
    print("✓ Git repository initialized")
    print("✓ Initial commit created")
    print("✓ Dependencies installed")
    print("✓ Tests executed")
    print("✓ GitHub setup scripts created")
    print("✓ PyCharm run configurations created")
    print("✓ Quick utility scripts created")

    print("\n🚀 To complete GitHub setup:")
    print("1. Run one of these commands in terminal:")
    print("   - Windows: setup_github.bat")
    print("   - Mac/Linux: bash setup_github.sh")
    print("\n   OR manually:")
    print("   - Install GitHub CLI: https://cli.github.com/")
    print("   - Run: gh auth login")
    print("   - Run: gh repo create gcc-emissions-calculator --private --source=. --push")

    print("\n🌐 To run the calculator:")
    print("1. API: Click 'Run API' in PyCharm run configurations (top right)")
    print("2. Web: Open docs/index.html in browser")
    print("3. Tests: Click 'Run Tests' in PyCharm run configurations")

    print("\n📱 Quick commands:")
    print("- Run everything: python run_all.py")
    print("- Just API: python -m src.api.app")
    print("- Just tests: pytest tests/")

    print("\n🎯 Final steps on GitHub.com:")
    print("1. Go to repository settings")
    print("2. Enable GitHub Pages from main branch /docs folder")
    print("3. Make repository public when ready")

    print("\n✨ Your calculator will be live at:")
    print("   https://[your-username].github.io/gcc-emissions-calculator/")


def main():
    """Run all setup tasks."""
    print("🚀 COMPLETE SETUP FOR GCC EMISSIONS CALCULATOR")
    print("=" * 60)

    # Change to project directory if needed
    if not os.path.exists("src"):
        print("❌ Error: Not in project directory. Please run from project root.")
        return

    # Run all setup tasks
    setup_git()
    configure_git()
    initial_commit()
    install_dependencies()
    run_tests()
    create_github_cli_config()
    create_run_configurations()
    create_quick_scripts()

    # Open in browser
    print("\n" + "=" * 60)
    print("🌐 Opening web interface...")
    print("=" * 60)
    open_in_browser()

    # Print final instructions
    print_final_instructions()


if __name__ == "__main__":
    main()