import os

files = ['1.txt', '2.txt']

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

sorted_files = sorted(files, key=count_lines)

output_filename = 'result.txt'

with open(output_filename, 'w', encoding='utf-8') as output_file:
    for filename in sorted_files:
        try:

            num_lines = count_lines(filename)


            output_file.write(f'{filename}\n{num_lines}\n')

            with open(filename, 'r', encoding='utf-8') as input_file:
                output_file.writelines(input_file.readlines())

            
            output_file.write('\n')
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")