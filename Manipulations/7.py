def copy_file(source_file, destination_file):
        with open(source_file, 'r') as f_source:
            content = f_source.read()

        with open(destination_file, 'w') as f_dest:
            f_dest.write(content)

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

copy_file(source_file, destination_file)

#Копирование содержимого файла в другой файл