import os
import time


directory = '.'

for dir_path, dir_names, file_names in os.walk(directory):
    for file_name in file_names:
        filepath = os.path.join(dir_path, file_name)
        filesize = os.path.getsize(filepath)
        filetime = time.strftime(
            '%d.%m.%Y %H:%M',
            time.localtime(os.path.getmtime(filepath))
        )
        parent_dir = os.path.basename(dir_path)
        print(
            f'Обнаружен файл: {file_name}\n'
            f'Путь: {filepath}\n'
            f'Размер: {filesize} байт\n'
            f'Время изменения: {filetime}\n'
            f'Родительская директория: {parent_dir}'
        )
        print('*' * 60)