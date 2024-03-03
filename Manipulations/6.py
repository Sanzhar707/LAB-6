import os

def generate_text_files():
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = f"{letter}.txt"
        with open(filename, 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")

generate_text_files()

#Генерация 26 текстовых файлов с именами A.txt, B.txt и так далее вплоть до Z.txt