import os

def check_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"\nPath '{path}' exists.\n")
        print(f"Filename: {filename}\n") 
        print(f"Directory: {directory}\n")
    else:
        print(f"Path '{path}' does not exist.")

given_path = input("Enter the path to test: ")
check_path(given_path)

#Проверка, существует данный путь или нет. Если путь существует, находит имя файла и часть каталога данного пути