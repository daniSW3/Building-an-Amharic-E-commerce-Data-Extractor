import os

# Define the base directory (can be "." for current directory or customize it)
base_dir = "Building-an-Amharic-E-commerce-Data-Extractor"

# Folder structure
folders = [
    ".vscode",
    ".github/workflows",
    "src",
    "notebooks",
    "tests",
    "scripts"
]

# Files to create: (path relative to base_dir, filename)
files = {
    ".vscode/settings.json": "",
    ".github/workflows/unittests.yml": "",
    ".gitignore": "",
    "requirements.txt": "",
    "README.md": "# Building-an-Amharic-E-commerce-Data-Extractor\n",
    "src/__init__.py": "",
    "notebooks/__init__.py": "",
    "notebooks/README.md": "# Notebooks\n",
    "tests/__init__.py": "",
    "scripts/__init__.py": "",
    "scripts/README.md": "# Scripts\n"
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Create files
for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Project structure for '{base_dir}' has been created.")
