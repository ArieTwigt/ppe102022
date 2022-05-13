import os

available_folders = []

# check if the file is a folder
current_files_folders = os.listdir()

# provide the list of folders
for file_folder in current_files_folders:
    if os.path.isdir(file_folder):
        if file_folder[0] == ".": # exclude hidden files like '.git'
            continue
        
        available_folders.append(file_folder)
    else:
        continue


# format and sort the availale folders
available_folders = "\t".join(sorted(available_folders))

# select the folder
folder_name = input(f"\nAvailable folders\n\n {available_folders}\n\nName of the folder:\n")

# format the folder name
folder_name = folder_name.replace(" ", "_").lower()

if folder_name not in current_files_folders:
    os.mkdir(folder_name)

# show the available files in the current folder
files_in_folder = os.listdir(folder_name)

available_files = []

for file in files_in_folder:
    if os.path.isfile(f"{folder_name}/{file}"):
        available_files.append(file)
        
# format and sort the available files
available_files = "\t".join(sorted(available_files))

# take the file name from the input
file_name = input(f"\nAvailable files\n\n {available_files}\n\nName of the file:\n")

# make sure we remove the extension from the file name
file_name = file_name.split(".")[0]

# decide the write_mode
write_mode = input("Do you want to overwrite?(Y/n)") or "y"

file_name = file_name.replace(" ", "_").lower()

if write_mode.lower() == "y":
    print(f"Inserted {write_mode}. We will overwrite the textfile")
    write_mode = "w"
else:
    print(f"Inserted {write_mode}. We will append to the textfile")
    write_mode = "a"


content = input("Insert your story:\n\n")

file_path = f"{folder_name}/{file_name}.txt"

with open(file_path, write_mode) as file:
    file.write(content)

print(f"Succesfully saved your content in: \n\n {file_path}")