# Python file detection

import os

file_path = "/home/junaid/Junaid/Coding/Python/Basic Syntax/51 - 77/59. File detection/stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does not exist")