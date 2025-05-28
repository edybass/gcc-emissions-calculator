#!/usr/bin/env python3
# Quick script to run all common tasks

import subprocess
import sys

print("🚀 Running all common tasks...")

# Install dependencies
print("\n📦 Installing dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run tests
print("\n🧪 Running tests...")
subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"])

# Start API
print("\n🌐 Starting API server...")
print("API will be available at: http://localhost:8000")
print("Press Ctrl+C to stop")
subprocess.run([sys.executable, "-m", "src.api.app"])
