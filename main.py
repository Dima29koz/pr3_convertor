import os
from typing import Optional

from PIL import Image, ImageFile, UnidentifiedImageError


def get_file_names(path: str):
    return os.listdir(path)


def get_image_obj(file_name) -> Optional[ImageFile.ImageFile]:
    try:
        image = Image.open(file_name)
    except FileNotFoundError:
        print('file not found')
        return
    except ValueError:
        print('file cant be read')
        return
    except UnidentifiedImageError:
        print('image cannot be opened and identified')
        return
    except TypeError:
        print('type error')
        return
    else:
        return image


def main():
    path = 'inputdata'
    files = get_file_names(path)
    images = [get_image_obj(f'{path + "/" + file}') for file in files]


if __name__ == '__main__':
    main()
