# React/Next.js Package Finder & Installer

This tool helps you identify and install all necessary npm packages for your React.js or Next.js projects. It consists of two components:

## 1. `main.py`
This script scans your project folder for package imports and generates a list of required packages in a `packages.txt` file.

### How to Use:
1. Run `main.py`.
2. Select the root folder of your project when prompted.
3. The script will scan all `.js`, `.jsx`, `.ts`, and `.tsx` files for package imports.
4. A `packages.txt` file will be created in the selected folder, listing all identified packages.

---

## 2. `install_packages.bat`
This batch script automates the installation of packages listed in the `packages.txt` file.

### How to Use:
1. Place `install_packages.bat` in the root directory of your project (where the `packages.txt` file is located).
2. Run the `.bat` file by double-clicking it or executing it in the Command Prompt.
3. The script will install all the packages listed in `packages.txt` using `npm install`.

---

## Reminder
If the directory you select contains multiple nested folders with React or Next.js projects, you must repeat this process for each folder individually.

---

## Example Workflow
1. Run `main.py` and select the root folder of your project.
2. Review the `packages.txt` file to ensure it contains all necessary packages.
3. Run `install_packages.bat` to install the packages in your project folder.

---

This tool simplifies dependency management, saving you time and effort when setting up your projects.
