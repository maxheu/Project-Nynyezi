import sys
from cx_Freeze import setup, Executable

setup(name="Project Nynyezi",
      version="5.1",
      description="Astronomie Spiel",
      executables = [Executable("nynyeni.py")])
