import os

def delete_file(file_path):    
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")

file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)

#Удаление файла по указанному пути