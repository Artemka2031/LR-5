from file_operations import operations
from config import categories, keywords_dict


def main():

    operations.create_to_sort_files(categories)
    operations.get_to_sort_files(keywords_dict)

if __name__ == '__main__':
    main()

