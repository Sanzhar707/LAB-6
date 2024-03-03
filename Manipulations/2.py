import os

def check_access(path):
    if os.access(path, os.R_OK): #R-Read
        print(f"Read access to '{path}' is allowed.")
    else:
        print(f"Read access to '{path}' is not allowed.")

    if os.access(path, os.W_OK): #W-Write
        print(f"Write access to '{path}' is allowed.")
    else:
        print(f"Write access to '{path}' is not allowed.")

    if os.access(path, os.X_OK): #X-Изменение
        print(f"Execute access to '{path}' is allowed.")
    else:
        print(f"Execute access to '{path}' is not allowed.")

specified_path = input("Enter the path to check access: ")
check_access(specified_path)

#Проверка доступа к указанному пути. Проверка на читаемость, возможность записи и исполняемость указанного пути