import json
import psutil
import os
import xml.etree.ElementTree as ET
import zipfile

# Получаем информацию о всех дисках
partitions = psutil.disk_partitions()

for partition in partitions:
    print(f"Название: {partition.device}")
    print(f"Тип файловой системы: {partition.fstype}")
    print(f"Тип диска: {partition.opts}")

    try:
        # Получаем информацию о размере и свободном месте
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Общий размер: {usage.total} байт")
        print(f"Свободное место: {usage.free} байт")
    except PermissionError:
        print("Нет доступа к этому разделу")

    print()  # Печатаем пустую строку для отделения информации о дисках

##############################
# Определяем директорию для создания файлов
file_directory = "C:/Users/valer/Documents/my_files"

# Убедимся, что директория существует, если нет — создадим
if not os.path.exists(file_directory):
    os.makedirs(file_directory)

# Функция для создания файла
def create_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'w') as file:
            print(f"Файл {filepath} создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

# Функция для записи строки в файл
def write_to_file(filename, content):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'a') as file:
            file.write(content + '\n')
            print(f"Строка записана в файл {filepath}.")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

# Функция для чтения файла
def read_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            print(f"Содержимое файла {filepath}:\n{content}")
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

# Функция для удаления файла
def delete_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        os.remove(filepath)
        print(f"Файл {filepath} удалён.")
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

# Работа с JSON

# Функция для создания JSON файла
def create_json_file(filename, json_data):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
            print(f"Файл {filepath} создан с содержимым: {json_data}")
    except Exception as e:
        print(f"Ошибка при создании JSON файла: {e}")

# Функция для чтения JSON файла
def read_json_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            print(f"Содержимое JSON файла {filepath}:")
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении JSON файла: {e}")

# Функция для удаления JSON файла
def delete_json_file(filename):
    delete_file(filename)

# Подменю для работы с JSON
def create_json_file(filename, json_data):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
            print(f"Файл {filepath} создан с содержимым: {json_data}")
    except Exception as e:
        print(f"Ошибка при создании JSON файла: {e}")

# Функция для чтения JSON файла
def read_json_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            print(f"Содержимое JSON файла {filepath}:")
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении JSON файла: {e}")

# Функция для удаления JSON файла
def delete_json_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        os.remove(filepath)
        print(f"Файл {filepath} удалён.")
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

# Функция для добавления ключа и значения в существующий или новый JSON файл
def add_key_value_to_json(filename, key, value):
    try:
        filepath = os.path.join(file_directory, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r+') as json_file:
                # Если файл существует, читаем данные и обновляем их
                data = json.load(json_file)
                data[key] = value
                json_file.seek(0)
                json.dump(data, json_file, indent=4)
                print(f"Добавлен ключ: {key}, значение: {value} в файл {filename}.")
        else:
            # Если файла нет, создаём новый с этим ключом и значением
            create_json_file(filename, {key: value})
    except Exception as e:
        print(f"Ошибка при добавлении ключа и значения в JSON файл: {e}")

# Подменю для работы с JSON
def json_menu():
    while True:
        print("\nМеню работы с JSON:")
        print("1. Создать JSON файл с ключом:значением")
        print("2. Добавить ключ:значение в существующий JSON файл")
        print("3. Прочитать JSON файл")
        print("4. Удалить JSON файл")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите имя JSON файла для создания (с расширением .json): ")
            key = input("Введите ключ: ")
            value = input("Введите значение: ")
            add_key_value_to_json(filename, key, value)
        elif choice == '2':
            filename = input("Введите имя JSON файла для добавления данных: ")
            key = input("Введите ключ: ")
            value = input("Введите значение: ")
            add_key_value_to_json(filename, key, value)
        elif choice == '3':
            filename = input("Введите имя JSON файла для чтения: ")
            read_json_file(filename)
        elif choice == '4':
            filename = input("Введите имя JSON файла для удаления: ")
            delete_json_file(filename)
        elif choice == '0':
            print()
            return

        else:
            print("Некорректный выбор, попробуйте снова.")


# Меню пользователя
def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Работа с файлами")
        print("2. Работа с JSON")
        print("3. Работа с XML")
        print("4. Работа с архивами")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            file_menu()
        elif choice == '2':
            json_menu()
        elif choice == '3':
            xml_menu()
        elif choice == '4':
            archive_menu()
        elif choice == '0':
            exit()
        else:
            print("Некорректный выбор, попробуйте снова.")


def file_menu():
    while True:
        print("\nМеню работы с файлами:")
        print("1. Создать файл")
        print("2. Записать строку в файл")
        print("3. Прочитать файл")
        print("4. Удалить файл")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите имя файла для создания: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Введите имя файла для записи: ")
            content = input("Введите строку для записи: ")
            write_to_file(filename, content)
        elif choice == '3':
            filename = input("Введите имя файла для чтения: ")
            read_file(filename)
        elif choice == '4':
            filename = input("Введите имя файла для удаления: ")
            delete_file(filename)
        elif choice == '0':
            print()
            return

        else:
            print("Некорректный выбор, попробуйте снова.")


def create_xml_file(filename, root_tag):
    try:
        root = ET.Element(root_tag)
        tree = ET.ElementTree(root)
        filepath = os.path.join(file_directory, filename)
        with open(filepath, 'wb') as file:
            tree.write(file, encoding='utf-8', xml_declaration=True)
        print(f"Файл {filepath} создан с корневым элементом <{root_tag}>.")
    except Exception as e:
        print(f"Ошибка при создании XML файла: {e}")


# Функция для записи новых данных в XML файл
def add_data_to_xml(filename, element_tag, element_text):
    try:
        filepath = os.path.join(file_directory, filename)
        tree = ET.parse(filepath)
        root = tree.getroot()

        new_element = ET.Element(element_tag)
        new_element.text = element_text
        root.append(new_element)

        tree.write(filepath, encoding='utf-8', xml_declaration=True)
        print(f"Добавлен элемент <{element_tag}>{element_text}</{element_tag}> в файл {filename}.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при добавлении данных в XML файл: {e}")


# Функция для чтения XML файла
def read_xml_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        tree = ET.parse(filepath)
        root = tree.getroot()
        print(f"Содержимое XML файла {filepath}:")
        for elem in root:
            print(f"<{elem.tag}>{elem.text}</{elem.tag}>")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении XML файла: {e}")


# Функция для удаления XML файла
def delete_xml_file(filename):
    try:
        filepath = os.path.join(file_directory, filename)
        os.remove(filepath)
        print(f"Файл {filepath} удалён.")
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")


# Подменю для работы с XML
def xml_menu():
    while True:
        print("\nМеню работы с XML:")
        print("1. Создать XML файл")
        print("2. Добавить элемент в XML файл")
        print("3. Прочитать XML файл")
        print("4. Удалить XML файл")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите имя XML файла для создания (с расширением .xml): ")
            root_tag = input("Введите корневой элемент: ")
            create_xml_file(filename, root_tag)
        elif choice == '2':
            filename = input("Введите имя XML файла для добавления данных: ")
            element_tag = input("Введите имя нового элемента: ")
            element_text = input("Введите текст для элемента: ")
            add_data_to_xml(filename, element_tag, element_text)
        elif choice == '3':
            filename = input("Введите имя XML файла для чтения: ")
            read_xml_file(filename)
        elif choice == '4':
            filename = input("Введите имя XML файла для удаления: ")
            delete_xml_file(filename)
        elif choice == '0':
            print()
            return
        else:
            print("Некорректный выбор, попробуйте снова.")


# Функция для создания zip архива
def create_zip_archive(archive_name):
    try:
        filepath = os.path.join(file_directory, archive_name)
        with zipfile.ZipFile(filepath, 'w') as archive:
            print(f"Создан архив {filepath}.")
    except Exception as e:
        print(f"Ошибка при создании архива: {e}")

# Функция для добавления файла в архив
def add_file_to_zip(archive_name, file_to_add):
    try:
        archive_path = os.path.join(file_directory, archive_name)
        file_path = os.path.join(file_directory, file_to_add)
        if os.path.exists(file_path):
            with zipfile.ZipFile(archive_path, 'a') as archive:
                archive.write(file_path, os.path.basename(file_path))
                print(f"Файл {file_to_add} добавлен в архив {archive_name}.")
        else:
            print(f"Файл {file_to_add} не найден.")
    except Exception as e:
        print(f"Ошибка при добавлении файла в архив: {e}")

# Функция для разархивирования файлов
def extract_zip_archive(archive_name):
    try:
        archive_path = os.path.join(file_directory, archive_name)
        extract_path = os.path.join(file_directory, "extracted")
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive.extractall(extract_path)
            print(f"Архив {archive_name} распакован в папку {extract_path}.")
    except FileNotFoundError:
        print(f"Архив {archive_name} не найден.")
    except Exception as e:
        print(f"Ошибка при разархивировании: {e}")

# Функция для удаления архива
def delete_zip_archive(archive_name):
    delete_file(archive_name)

# Функция для получения размера архива
def get_zip_size(archive_name):
    try:
        archive_path = os.path.join(file_directory, archive_name)
        if os.path.exists(archive_path):
            size = os.path.getsize(archive_path)
            print(f"Размер архива {archive_name}: {size} байт.")
        else:
            print(f"Архив {archive_name} не найден.")
    except Exception as e:
        print(f"Ошибка при получении размера архива: {e}")

# Подменю для работы с архивами
def archive_menu():
    while True:
        print("\nМеню работы с архивами:")
        print("1. Создать архив")
        print("2. Добавить файл в архив")
        print("3. Разархивировать файл")
        print("4. Определить размер архива")
        print("5. Удалить архив")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            archive_name = input("Введите имя архива (с расширением .zip): ")
            create_zip_archive(archive_name)
        elif choice == '2':
            archive_name = input("Введите имя архива (с расширением .zip): ")
            file_to_add = input("Введите имя файла для добавления в архив: ")
            add_file_to_zip(archive_name, file_to_add)
        elif choice == '3':
            archive_name = input("Введите имя архива для разархивирования (с расширением .zip): ")
            extract_zip_archive(archive_name)
        elif choice == '4':
            archive_name = input("Введите имя архива для определения размера (с расширением .zip): ")
            get_zip_size(archive_name)
        elif choice == '5':
            archive_name = input("Введите имя архива для удаления (с расширением .zip): ")
            delete_zip_archive(archive_name)
        elif choice == '0':
            return
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()

# Запуск программы
main_menu()
