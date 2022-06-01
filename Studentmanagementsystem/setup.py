import sys

from cx_Freeze import*
includefiles = ["mahi.ico"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", #Directory_
     "RmstuCseStudentManagementSystem", #Name
     "TARGETDIR", #Component_
     "[TARGETDIR]\RmstuCseStudentManagementSystem.exe", #Target
     None, # Arguments
     None, # Description
     None, # Hotkey
     None, # Icon
     None, # Icondex
     None, # ShowCmd
     "TARGETDIR", # WKDir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Cse Student Management System Developed By Sujan",
    author="Mahir adnan Sujan",
    name="RmstuCseStudentManagementSystem",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="Student.py",
            base=base,
            icon='mahi.ico',
        )
    ]

)