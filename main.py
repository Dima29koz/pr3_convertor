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


def save_with_extension(image: ImageFile.ImageFile, file_name: str, extension: str):
    if extension not in ['jpg', 'png', 'tif', 'gif', 'bmp']:
        print("Данное расширение не поддерживается")
        return
    rgb_im = image.convert('RGB')
    try:
        rgb_im.save(f'out/{file_name}.{extension}')
    except TypeError:
        rgb_im.save(f'tmp/{file_name}.jpg')
        img = get_image_obj(f'tmp/{file_name}.jpg')
        print(f'[SAVED TMP] {img.filename} -> {file_name}.jpg')

        save_with_extension(img, file_name, extension)
    else:
        print(f'[SAVED] {image.filename} -> {file_name}.{extension}')
        return True


def main():
    path = 'inputdata'
    files = get_file_names(path)
    for file in files:
        image = get_image_obj(f'{path + "/" + file}')
        if image:
            file_name, ext = os.path.splitext(file)
            extension = str(input(f'Укажите конечное расширение для файла {file}: '))
            save_with_extension(image, file_name, extension if extension else 'jpg')
            # for ex in ['jpg', 'png', 'tif', 'gif', 'bmp']:
            #     save_with_extension(image, file_name, ex)


if __name__ == '__main__':
    main()
