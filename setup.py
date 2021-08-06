from cx_Freeze import setup, Executable
executables = [Executable("screen.py", base=None)]
packages = ["idna"]
setup(
    executables = executables
)
