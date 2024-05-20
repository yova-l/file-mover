import unittest
#https://docs.python.org/3/library/unittest.html

import sys
sys.path.append("..")

import os
import shutil
import filecmp

from ..model.FileMover import FileMover

JPGS_PATH = "./jpgs/"
RAWS_PATH = "./raws/"
RAW_FOLDER_NAME = "MyRaws"

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class MovingFiles(unittest.TestCase):
    # def _restore_folders():
    #     os.

    def test_all_expected_files_are_there(self):
        mfm = FileMover()
        mfm.setJpgsPath(JPGS_PATH)
        mfm.setRawsPath(RAWS_PATH)
        mfm.wantFolder()
        mfm.setFolderName(RAW_FOLDER_NAME)
        mfm.moveRaws()

        

if __name__ == '__main__':
    unittest.main()