import os

os.chdir('../venv')

for filename in os.listdir('../venv'):
    if os.path.isdir(filename):
        print("Dir", filename)
    else:
        print('File', filename)
