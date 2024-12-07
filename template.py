import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "textSummerizer"

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for file in list_of_files:
    file_path = Path(file)
    file_dir = file_path.parent  # Parent directory
    filename = file_path.name   # File name

    try:
        # Create directories if they do not exist
        if file_dir != Path(""):
            file_dir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {file_dir}")

        # Create the file if it does not exist or is empty
        if not file_path.exists() or file_path.stat().st_size == 0:
            with open(file_path, 'w') as f:
                # Add default content to specific files if required
                if filename == "config.yaml":
                    f.write("# Default configuration file\n")
                elif filename == "params.yaml":
                    f.write("# Default parameter file\n")
                elif filename.endswith(".py"):
                    f.write("# Python module\n")
                logging.info(f"Created empty file: {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")

    except Exception as e:
        logging.error(f"Failed to create {file}: {e}")
