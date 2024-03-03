def write_list_to_file(my_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in my_list:
            f.write(str(i) + '\n')

my_list = ['first', 'second', 'third', 'last']
file_name = 'output.txt'

write_list_to_file(my_list, file_name)

#Запись списка в файл