#!/bin/bash

# Simple wrapper for the Python template creator
# This provides backwards compatibility with the old bash script

# Default value
PROJECT_NAME=${1:-"rhs-altium-template"}

# Run the Python script
python3 create_template.py --name "$PROJECT_NAME"