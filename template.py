# import os
# from pathlib import Path
# import logging
#
# logging.basicConfig(
#     level = logging.INFO,
#     format = "[%(asctime)s: %(levelname)s]: %(message)s"
# )
#
# while True:
#     project_name = input("Enter your project name: ")
#     if project_name !='':
#         break
#
# logging.info(f"Creating project by name: {project_name}")
#
# list_of_files = [
#
#    # f"src/{project_name}/__init__.py",
#     f"{project_name}/__init__.py",
#     f"{project_name}/components/__init__.py",
#     f"{project_name}/config/__init__.py",
#     f"{project_name}/constant/__init__.py",
#     f"{project_name}/entity/__init__.py",
#     f"{project_name}/exception/__init__.py",
#     f"{project_name}/logger/__init__.py",
#     f"{project_name}/pipeline/__init__.py",
#     f"{project_name}/utils/__init__.py",
#     f"configs/config.yaml",
#     "schema.yaml",
#     "requirements.txt",
#     "setup.py",
#     "main.py",
#     "app.py",
#     #"logs.py",
#     #"exception.py"
# ]
#
#
# for filepath in list_of_files:
#     filepath = Path(filepath)
#     filedir, filename = os.path.split(filepath)
#     if filedir !="":
#         os.makedirs(filedir, exist_ok=True)
#         logging.info(f"Creating a new directory at : {filedir} for file: {filename}")
#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         with open(filepath, "w") as f:
#             pass
#             logging.info(f"Creating a new file: {filename} for path: {filepath}")
#     else:
#         logging.info(f"file is already present at: {filepath}")

import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

# 1. Folders with multiple files (Dictionary: key -> list of files)
folder_structure = {
    "pages": [
        "home_page.py",
        "registration_page.py",
        "login_page.py",
        "logout_page.py",
        "my_account_page.py",
        "product_page.py",
        "search_results_page.py",
        "shopping_cart_page.py",
        "__init__.py",
    ],
    "testdata": [
        "logindata.json",
        "logindata.csv",
        "logindata.xlsx",
        "__init__.py",
    ],
    "utilities": [
        "random_data_util.py",
        "data_reader_util.py",
        "__init__.py",
    ],
}

# 2. Standalone files and single-file folders (List of strings)
list_of_files = [
    "reports/__init__.py",
    "tests/__init__.py",
    "config.py",
    "conftest.py",
    "pytest.ini",
]

# 3. Combine the dictionary entries into list_of_files
for folder, files in folder_structure.items():
    for file in files:
        list_of_files.append(f"{folder}/{file}")

# 4. Create all folders and empty files
for filepath in list_of_files:
    path = Path(filepath)
    if path.parent != Path("."):
        path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"Created empty file: {path}")
    else:
        logging.info(f"File already exists: {path}")