# Text-Summerizer-NLP-Project

# This repository contains the foundational setup for a Python project called TextSummerizer, designed for summarizing text efficiently. The included script automates the creation of directories and files, making it easier to start and maintain a structured Python project.





# textSummerizer/
├── .github/
│   └── workflows/
│       └── .gitkeep          # Placeholder for GitHub Actions workflows
├── src/
│   └── textSummerizer/
│       ├── __init__.py       # Package initialization
│       ├── components/       # Components of the project
│       │   └── __init__.py
│       ├── utils/            # Utility functions
│       │   ├── __init__.py
│       │   └── common.py
│       ├── logging/          # Logging utilities
│       │   └── __init__.py
│       ├── config/           # Configuration files
│       │   ├── __init__.py
│       │   └── configuration.py
│       ├── pipeline/         # Pipeline for execution
│       │   └── __init__.py
│       ├── entity/           # Entity definitions
│       │   └── __init__.py
│       └── constants/        # Project constants
│           └── __init__.py
├── config/
│   └── config.yaml           # Configuration file
├── params.yaml               # Project parameters
├── main.py                   # Entry point of the project
├── Dockerfile                # Docker containerization file
├── requirements.txt          # Python dependencies
├── setup.py                  # Project setup script
├── research/
│   └── trials.ipynb          # Experimentation notebook

# Work flow of the project 

1. Update config.yaml
2. Update Params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py
