import pathlib

file_path = pathlib.Path.home() / "my_folder" / "my_file.txt"

print(file_path)
print(file_path.exists())
print(file_path.name)
print(file_path.parent.name)