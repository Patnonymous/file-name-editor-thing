# Imports
import os
import os.path
import glob
from pathlib import Path

# Functions.
def main():
    print("Starting!")
    total_files = 0
    # Get dir.
    working_dir = directory_input()

    print("\nGiven path is: ", working_dir)
    path_list = Path(working_dir).rglob("*.*")
    # Count files.
    for filepath in glob.iglob(working_dir + "\*"):
        isDir = os.path.isdir(filepath)
        if not isDir:
            print(f"Found item {filepath}. isDir: ", isDir)
            total_files = total_files + 1
    print(f"There are {total_files} items in the directory.")

    print("\nEnter the base name for the files when renaming.")
    print("The incrementing numbers will be added right at the end of the files name.")
    print("Ex. Base name MyFile will become MyFile0, MyFile1, MyFile2, MyFile3, and so on.")
    base_name = input("Enter base name: ")

    print("\nEnter the skip number. When renaming, the new files will start at this number.")
    print("Ex. You enter 6, new files will be named MyFile6, MyFile7, MyFile8 and so on.")
    skip_number = input("Enter skip num: ")

    rename_files(base_name, working_dir, total_files, skip_number)




def directory_input():
    print("Please enter the directory containing your files.")
    user_dir_entry = input("Path: ")
    user_dir_entry = os.path.normpath(user_dir_entry)
    return user_dir_entry


def rename_files(base_name, working_dir, total_files, skip_number):
    print("\nRenaming files. Will use base name: ", base_name)
    print("Will start at: ", skip_number)
    f_num = 0
    skip_number = int(skip_number)

    for item_path in glob.iglob(working_dir + "\*"):
        isDir = os.path.isdir(item_path)
        if not isDir:
            item_name, item_extension = os.path.splitext(item_path)
            print("\nItem name: ", item_name)
            print("Extension: ", item_extension)
            print(f"File number {f_num + 1} of {total_files}.")
            # Create new name using base name, f num, and the files extension.
            new_name = working_dir + '\\' + base_name + str(skip_number) + item_extension
            # Do the rename.
            os.rename(item_path, new_name)
            f_num = f_num + 1
            skip_number = skip_number + 1
# Run.
main()
