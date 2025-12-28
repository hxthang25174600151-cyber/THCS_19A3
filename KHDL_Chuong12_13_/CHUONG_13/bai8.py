
import os
os.makedirs("temp_files",exist_ok=True)
open("temp_files/file.txt","w").close()
os.rename("temp_files/file.txt","temp_files/new_file.txt")
os.rename("temp_files/new_file.txt","new_file.txt")
os.rmdir("temp_files")
