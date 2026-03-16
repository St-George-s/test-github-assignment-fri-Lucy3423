#!/bin/bash

# Function to check if Poetry is installed
check_poetry() {
    if ! command -v poetry &> /dev/null
    then
        echo "Poetry could not be found. Installing Poetry..."
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    else
        echo "Poetry is already installed."
    fi
}

# Check and install Poetry if necessary
check_poetry

# Install dependencies and create the virtual environment
echo "Installing dependencies..."
poetry install

# Run the main script
echo "Running the main script..."
poetry run python setup/main.py
