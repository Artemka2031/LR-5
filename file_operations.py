from pathlib import Path


class File_operations:
    def __init__(self):
        self.to_sort = Path("To_sort_docs")
        self.sorted = Path("Sorted_docs")

    def create_to_sort_files(self, categories : dict):
        # Проверяем, что папка "To_sort_docs" существует, иначе создаем ее
        if not self.to_sort.exists():
            self.to_sort.mkdir()

        for category, category_array in categories.items():
            for category_name, category_text in category_array:
                file_name = f"{category_name}.txt"
                file_path = self.to_sort / file_name

                # Проверяем, существует ли файл перед созданием
                if not file_path.exists():
                    with open(file_path, "w") as file:
                        # Записываем в файл текст
                        file.write(category_text)

    def get_to_sort_files(self):
        # Используем генератор списка для получения путей ко всем файлам в папке to_sort
        return [file for file in self.to_sort.iterdir() if file.is_file()]



operations = File_operations()
