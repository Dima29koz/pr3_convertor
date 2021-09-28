import unittest

from PIL import ImageFile
from main import get_file_names, get_image_obj


class CalculateCase(unittest.TestCase):

    def test_get_files(self):
        files = get_file_names('inputdata')
        self.assertEqual(files, ['1.png', '2.bmp', '3.jpg', '4.gif', '5.tif'])

    def test_get_image(self):
        image = get_image_obj('inputdata/1.png')
        self.assertTrue(isinstance(image, ImageFile.ImageFile) or image is None)
