# Codebase Analyzer

This Python project helps users understand a codebase by generating descriptions for each file and saving them in a structured format.

## Table of Contents

- Installation
- Usage
- Project Structure

## Installation

1. Install Python
2. Set your `GOOGLE_API_KEY` in environment variable.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your codebase directoyr name is placed in the `CODE_DIR` constant.
2. Run the main script to generate file descriptions:
    ```bash
    python main.py
    ```
3. The descriptions will be saved in the `result` directory, maintaining the original directory structure.

## Project Structure

- `data/`: Directory containing the codebase to be analyzed.
- `result/`: Directory where the generated descriptions will be saved.
- `utils.py`: Contains utility functions for file operations.
- `llm.py`: Contains functions for generating file descriptions and sequences.
- `main.py`: Main script to run the analysis.

