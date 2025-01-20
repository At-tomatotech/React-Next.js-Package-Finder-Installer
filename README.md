# React-Next.js-Package-Finder-Installer
This tool helps you identify and install all necessary npm packages for your React.js or Next.js projects. It consists of two components:

1. main.py
This script scans your project folder for package imports and generates a list of required packages in a packages.txt file.

How to Use:
Run main.py.
Select the root folder of your project when prompted.
The script will scan all .js, .jsx, .ts, and .tsx files for package imports.
A packages.txt file will be created in the selected folder, listing all identified packages.
2. install_packages.bat
This batch script automates the installation of packages listed in the packages.txt file.

How to Use:
Place install_packages.bat in the root directory of your project (where the packages.txt file is located).
Run the .bat file by double-clicking it or executing it in the Command Prompt.
The script will install all the packages listed in packages.txt using npm install.
Reminder
If the directory you select contains multiple nested folders with React or Next.js projects, you must repeat this process for each folder individually.

Example Workflow
Run main.py and select the root folder of your project.
Review the packages.txt file to ensure it contains all necessary packages.
Run install_packages.bat to install the packages in your project folder.
This tool simplifies dependency management, saving you time and effort when setting up your projects.
