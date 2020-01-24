
# Copyright (c) 2020 Alexandre Quenon - UMONS



import unittest

import threading
import time
import pyautogui
pyautogui.PAUSE = 1.0
pyautogui.FAILSAFE = True

from pathlib import Path
from pandas import DataFrame

import greatpublicationplanner._file_manager as file_manager


class PressThread(threading.Thread):
    """
    A thread for automatic testing in GUI mode.

    The thread must be paused immediately after being run to be sure that the GUI has been started before controlling it.
    """

    def __init__(self, cmd, msg):
        super(PressThread, self).__init__()
        self.commands = cmd
        self.message = msg

    def run(self):
        time.sleep(1.0)
        if self.message:
            pyautogui.typewrite(self.message)
            time.sleep(1.0)
        pyautogui.press(self.commands)


class FileManagerTest(unittest.TestCase):

    # Test suite: open file
    def test_open_file_gui__click_cancel(self):
        t = PressThread(cmd=['tab', 'tab', 'enter'], msg='Automatic cancel')
        t.start()

        with self.assertRaises(FileNotFoundError):
            file_manager.open_file_gui()
    
    def test_open_file_shell__file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            file_manager.open_file_shell("./greatpublicationplanner/tests/examples/toto.csv")


    # Test suite: dump data
    def test_dump_data_shell__directory_not_found(self):
        with self.assertRaises(NotADirectoryError):
            file_manager.dump_data_shell(None, "./greatpublicationplanner/toto/dump_data.csv")


    # Test suite: read file
    def test_read_file__not_supported(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.toto")
        with self.assertRaises(ValueError):
            file_manager.read_file(target_file)
    
    def test_read_file__csv(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.csv")
        conf = file_manager.read_file(target_file)
        self.assertIsInstance(conf, DataFrame)

    def test_read_file__xls(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.xls")
        conf = file_manager.read_file(target_file)
        self.assertIsInstance(conf, DataFrame)

    def test_read_file__xlsx(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.xlsx")
        conf = file_manager.read_file(target_file)
        self.assertIsInstance(conf, DataFrame)
    

    # Test suite: write file
    def test_write_file__not_supported(self):
        target_file = Path("./greatpublicationplanner/tests/dump_data.toto")
        with self.assertRaises(ValueError):
            file_manager.read_file(target_file)
        
    def test_write_file__csv(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.csv")
        conf = file_manager.read_file(target_file)
        
        target_file = Path("./greatpublicationplanner/tests/dump_data.csv")
        file_manager.write_file(conf, target_file)
        dump = file_manager.read_file(target_file)
        self.assertTrue(dump.equals(conf))
        target_file.unlink()
    
    def test_write_file__xls(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.xls")
        conf = file_manager.read_file(target_file)

        target_file = Path("./greatpublicationplanner/tests/dump_data.xls")
        file_manager.write_file(conf, target_file)
        dump = file_manager.read_file(target_file)
        self.assertTrue(dump.equals(conf))
        target_file.unlink()

    def test_write_file__xlsx(self):
        target_file = Path("./greatpublicationplanner/tests/examples/list_conf.xlsx")
        conf = file_manager.read_file(target_file)

        target_file = Path("./greatpublicationplanner/tests/dump_data.xlsx")
        file_manager.write_file(conf, target_file)
        dump = file_manager.read_file(target_file)
        self.assertTrue(dump.equals(conf))
        target_file.unlink()
