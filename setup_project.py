import os

# Define the full folder structure
folders = [
    ".vscode",
    ".github/workflows",
    "data/raw",
    "notebooks",
    "src",
    "tests",
    "scripts"
]

# Define initial files to be created
files = {
    ".gitignore": "__pycache__/\n.venv/\n.env\n*.py[cod]",
    "requirements.txt": "pandas\nnumpy\nnltk\npytest",
    "README.md": "# News Sentiment Analysis",
    "src/__init__.py": "",
    "tests/__init__.py": "",
    "notebooks/__init__.py": "",
    "scripts/__init__.py": ""
}

def main():
    # Create Folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create Files
    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)
        print(f"Created file: {path}")

    print("\n✅ Structure built successfully!")

if __name__ == "__main__":
    main()