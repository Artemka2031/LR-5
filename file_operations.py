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
                    with open(file_path, "w", encoding='UTF-8') as file:
                        # Записываем в файл текст
                        file.write(category_text)

    def get_to_sort_files(self, keyword_dict: dict):

        if not self.sorted.exists():
            self.sorted.mkdir()

            # Create folders based on keyword_dict values

        # Create folders based on keyword_dict values
        for category in keyword_dict.keys():
            category_folder = self.sorted / category
            if not category_folder.exists():
                category_folder.mkdir()

        # Iterate through the files in the "To_sort_docs" directory
        for file_path in self.to_sort.iterdir():
            if file_path.is_file():
                # Get the filename without extension (the stem)
                filename_without_extension = file_path.stem

                # Iterate through the keyword_dict to find matching keywords
                for keyword, category_array in keyword_dict.items():
                    sorted_path = self.sorted / keyword / file_path.name
                    if any(keyword in filename_without_extension for keyword in category_array):
                        # Check if the file still exists before moving it
                        if file_path.exists():
                            for category in keyword_dict.keys():
                                file_path.rename(sorted_path)
                                break

operations = File_operations()
