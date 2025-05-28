#!/bin/bash
# GitHub Setup Script
# Run this to create and configure your GitHub repository

REPO_NAME="gcc-emissions-calculator"
REPO_DESCRIPTION="Greenhouse Gas Emissions Calculator for GCC countries (UAE & Saudi Arabia)"

echo "Setting up GitHub repository: $REPO_NAME"
echo "==========================================="

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) is not installed."
    echo "Install it from: https://cli.github.com/"
    echo "Or run: winget install --id GitHub.cli"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "Please authenticate with GitHub:"
    gh auth login
fi

# Create repository
echo "Creating repository..."
gh repo create $REPO_NAME --private --description "$REPO_DESCRIPTION" --source=. --remote=origin --push

echo "Repository created!"
echo "URL: https://github.com/$(gh api user --jq .login)/$REPO_NAME"

# Enable GitHub Pages
echo "Enabling GitHub Pages..."
gh api repos/$(gh api user --jq .login)/$REPO_NAME/pages   --method POST   --field source='{"branch":"main","path":"/docs"}'   2>/dev/null || echo "Pages might already be enabled or need manual setup"

echo ""
echo "Next steps:"
echo "1. Go to: https://github.com/$(gh api user --jq .login)/$REPO_NAME/settings/pages"
echo "2. Verify Pages is enabled from main branch /docs folder"
echo "3. Your site will be at: https://$(gh api user --jq .login).github.io/$REPO_NAME/"
echo ""
echo "To make repository public later:"
echo "gh repo edit $REPO_NAME --visibility public"
