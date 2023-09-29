from file_operations import operations
from config import categories


def main():

    operations.create_to_sort_files(categories.encode('windows-1252'))


if __name__ == '__main__':
    main()

