"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html


Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.
"""
import os
import shutil

new_catalog = 'my_project_new\\templates'
for root, dirs, files in os.walk('my_project'):
    for file in files:
        if file.endswith(".html"):
            templates_catalog = os.path.basename(os.path.dirname(os.path.join(root, file)))
            if not os.path.exists(os.path.join(new_catalog, templates_catalog)):
                os.makedirs(os.path.join(new_catalog, templates_catalog))
                shutil.copy(os.path.join(root, file), os.path.join(new_catalog, templates_catalog))
            else:
                shutil.copy(os.path.join(root, file), os.path.join(new_catalog, templates_catalog))
