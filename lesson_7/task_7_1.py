"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os

mid_folder = 'my_project'
end_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(mid_folder):
    for end_folder in end_folders:
        os.makedirs(os.path.join(mid_folder, end_folder))
    print('... Стартер для проекта успешно создан в текущей директории')
else:
    print(f'{mid_folder} уже существует')
