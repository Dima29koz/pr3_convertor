import unittest

from PIL import ImageFile
from main import ImageConverter


class CalculateCase(unittest.TestCase):

    def test_get_files(self):
        ic = ImageConverter()
        files = ic.get_file_names()
        self.assertEqual(files, ['1.png', '2.bmp', '3.jpg', '4.gif', '5.tif'])

    def test_get_image(self):
        ic = ImageConverter()
        image = ic.get_image_obj(f'{ic.path}/1.png')
        self.assertTrue(isinstance(image, ImageFile.ImageFile) or image is None)

    def test_save_image(self):
        ic = ImageConverter()
        image = ic.get_image_obj(f'{ic.path}/1.png')
        self.assertTrue(ic.save_with_extension(image, 'test', 'jpg'))
