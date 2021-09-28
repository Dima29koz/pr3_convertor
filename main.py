import os


def get_file_names(path: str):
    return os.listdir(path)


def main():
    path = 'inputdata'
    files = get_file_names(path)


if __name__ == '__main__':
    main()
