#!/bin/bash

# Simple wrapper for the Python template creator
# This provides backwards compatibility with the old bash script

# Default values
PROJECT_NAME=${1:-"rhs-altium-template"}
INCLUDE_ALTLIB=${2:-"false"}

# Convert bash boolean to Python flag
if [ "$INCLUDE_ALTLIB" = "false" ]; then
    ALTLIB_FLAG="--no-altlib"
else
    ALTLIB_FLAG=""
fi

# Run the Python script
python3 create_template.py --name "$PROJECT_NAME" $ALTLIB_FLAG
