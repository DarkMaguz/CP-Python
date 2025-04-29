#!/bin/bash

# Exit if any command fails
set -e

# Remove virtual environment if it exists
if [ -d ".venv" ]; then
  rm -rf .venv
fi

# Create a fresh virtual environment and activate it
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
