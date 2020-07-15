import subprocess
import os
print("Starting...")
print("Converting...")
(stat, output) = subprocess.getstatusoutput("python ExampleScript.py build")
print("Done...At "+os.getcwd)
