"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""
import os

with open('config.yaml', encoding='utf-8') as config:
    folder_my_project = (config.readline().strip('| -\n'))
    folder_settings = (config.readline().strip('| -\n'))
    files_setting = (config.readline().strip('| -\n').split(', '))
    folder_mainapp = (config.readline().strip('| -\n'))
    files_mainapp = (config.readline().strip('| -\n').split(', '))
    folder_templates_in_mainapp = (config.readline().strip('| -\n'))
    folder_mainapp_in_templates = (config.readline().strip('| -\n'))
    files_mainapp_in_templates = (config.readline().strip('| -\n').split(', '))
    folder_authapp = (config.readline().strip('| -\n'))
    files_authapp = (config.readline().strip('| -\n').split(', '))
    folder_templates_in_authapp = (config.readline().strip('| -\n'))
    folder_authapp_in_templates = (config.readline().strip('| -\n'))
    files_authapp_in_templates = (config.readline().strip('| -\n').split(', '))

    os.makedirs(f'{folder_my_project}\\{folder_settings}')
    os.makedirs(f'{folder_my_project}\\{folder_mainapp}')
    os.makedirs(f'{folder_my_project}\\{folder_mainapp}\\{folder_templates_in_mainapp}\\{folder_mainapp_in_templates}')
    os.makedirs(f'{folder_my_project}\\{folder_authapp}')
    os.makedirs(f'{folder_my_project}\\{folder_authapp}\\{folder_templates_in_authapp}\\{folder_authapp_in_templates}')
    for file_setting in files_setting:
        add_files = open(os.path.join(folder_my_project, folder_settings, file_setting), 'w')
        add_files.close()
    for file_mainapp in files_mainapp:
        add_files = open(os.path.join(folder_my_project, folder_mainapp, file_mainapp), 'w')
        add_files.close()
    for file_mainapp_in_templates in files_mainapp_in_templates:
        add_files = open(os.path.join(folder_my_project, folder_mainapp, folder_templates_in_mainapp,
                                      folder_mainapp_in_templates, file_mainapp_in_templates), 'w')
        add_files.close()
    for file_authapp in files_authapp:
        add_files = open(os.path.join(folder_my_project, folder_authapp, file_authapp), 'w')
        add_files.close()
    for file_authapp_in_templates in files_authapp_in_templates:
        add_files = open(os.path.join(folder_my_project, folder_authapp, folder_templates_in_authapp,
                                      folder_authapp_in_templates, file_authapp_in_templates), 'w')
        add_files.close()

print('... Стартер для проекта успешно создан в текущей директории')
