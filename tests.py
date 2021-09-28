import unittest

from main import get_file_names


class CalculateCase(unittest.TestCase):

    def test_get_files(self):
        files = get_file_names('inputdata')
        self.assertEqual(files, ['1.png', '2.bmp', '3.jpg', '4.gif', '5.tif'])
