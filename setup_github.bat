@echo off
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
gh api repos/%USERNAME%/%REPO_NAME%/pages --method POST --field source="{"branch":"main","path":"/docs"}" 2>nul || echo Pages might already be enabled or need manual setup

echo.
echo Next steps:
echo 1. Go to: https://github.com/%USERNAME%/%REPO_NAME%/settings/pages
echo 2. Verify Pages is enabled from main branch /docs folder
echo 3. Your site will be at: https://%USERNAME%.github.io/%REPO_NAME%/
echo.
echo To make repository public later:
echo gh repo edit %REPO_NAME% --visibility public
