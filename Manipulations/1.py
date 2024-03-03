import os #Для работы с операционными системами

def list_directories_and_files(path):
        with os.scandir(path) as path: #Сканируем директорию
            for entry in path:
                if entry.is_dir():
                    print(f"Directory: {entry.name}")
                elif entry.is_file():
                    print(f"File: {entry.name}")

specified_path = input("Enter the path to list directories and files: ")
list_directories_and_files(specified_path)

#Выводит список файлов и всех директорий по указанному пути.