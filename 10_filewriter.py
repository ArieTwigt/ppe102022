import os

available_files_folders = "\n".join(os.listdir())


folder_name = input(f"Name of the folder:\n Available folders\n {available_files_folders}\n")
file_name = input("Name of the file:\n")
write_mode = input("Do you want to overwrite?(Y/n)") or "y"

folder_name = folder_name.replace(" ", "_").lower()
file_name = file_name.replace(" ", "_").lower()

if write_mode.lower() == "y":
    print(f"Inserted {write_mode}. We will overwrite the textfile")
    write_mode = "w"
else:
    print(f"Inserted {write_mode}. We will append to the textfile")
    write_mode = "a"


current_files_folders = os.listdir()

if folder_name not in current_files_folders:
    os.mkdir(folder_name)


content = input("Insert your story:\n\n")

file_path = f"{folder_name}/{file_name}.txt"

with open(file_path, write_mode) as file:
    file.write(content)

print(f"Succesfully saved your content in: \n\n {file_path}")