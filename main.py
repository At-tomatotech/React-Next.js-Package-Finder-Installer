import os
import re
from tkinter import Tk, filedialog

def select_folder():
    """Opens a dialog to select a folder and returns the selected path."""
    Tk().withdraw()  # Hides the root Tkinter window
    folder = filedialog.askdirectory(title="Select Your Project Folder")
    if not folder:
        print("No folder selected. Exiting...")
        exit()
    return folder

def is_local_path(import_path):
    """Checks if the import path is a local module path."""
    return import_path.startswith(('./', '../', '@/'))

def find_imports(folder_path):
    """Finds all 'import { } from '(package)';' statements in the given folder."""
    package_set = set()
    # Supported file extensions for React/Next.js projects
    extensions = (".js", ".jsx", ".ts", ".tsx")
    pattern = re.compile(r"import\s+.*?\s+from\s+['\"](.+?)['\"];")

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = pattern.findall(content)
                        for match in matches:
                            if not is_local_path(match):  # Exclude local paths
                                package_set.add(match)
                except (UnicodeDecodeError, FileNotFoundError):
                    print(f"Error reading file: {file_path}")

    return sorted(package_set)

def save_packages_to_file(packages, folder_path):
    """Saves the list of packages to a file."""
    save_path = os.path.join(folder_path, "packages.txt")
    try:
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(packages))
        print(f"\nPackage list saved to: {save_path}")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    print("Welcome to the React/Next.js Package Finder!")
    folder_path = select_folder()
    print(f"Scanning folder: {folder_path}")
    
    packages = find_imports(folder_path)
    
    if packages:
        print("\nPackages found:")
        for pkg in packages:
            print(f"- {pkg}")
        save_packages_to_file(packages, folder_path)
    else:
        print("\nNo packages found in the selected folder.")

if __name__ == "__main__":
    main()
