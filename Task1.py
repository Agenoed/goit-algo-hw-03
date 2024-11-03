import os
import shutil
import argparse

def copy_and_sort_files(source_dir, dest_dir):
    try:
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isfile(item_path):
                # Отримуємо розширення файлу
                _, ext = os.path.splitext(item)
                ext = ext[1:].lower()  # Видаляємо крапку та приводимо до нижнього регістру

                # Створюємо піддиректорію для розширення, якщо її ще немає
                subdir_path = os.path.join(dest_dir, ext)
                os.makedirs(subdir_path, exist_ok=True)

                # Копіюємо файл у піддиректорію
                shutil.copy2(item_path, subdir_path)
                print(f"Скопійовано файл '{item}' до '{subdir_path}'")

            elif os.path.isdir(item_path):
                # Рекурсивно обробляємо піддиректорію
                copy_and_sort_files(item_path, dest_dir)

    except OSError as e:
        print(f"Помилка: {e}")

def main():

    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    copy_and_sort_files(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()