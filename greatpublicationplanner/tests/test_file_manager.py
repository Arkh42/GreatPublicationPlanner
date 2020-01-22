
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

    # suite_open_file_gui
    def test_open_file_gui__click_cancel(self):
        t = PressThread(cmd=['tab', 'tab', 'enter'], msg='Automatic cancel')
        t.start()

        with self.assertRaises(FileNotFoundError):
            file_manager.open_file_gui()
    
    # suite_open_file_shell
    def test_open_file_shell__file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            file_manager.open_file_shell("./greatpublicationplanner/tests/examples/toto.csv")
    
    # suite_read_file
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



# def test_open_file_gui_suite():
#     suite_open_file_gui = unittest.TestSuite()
#     suite_open_file_gui.addTest(WidgetTestCase('test_open_file_gui__click_cancel'))
#     return suite_open_file_gui

# def test_open_file_shell_suite():
#     suite_open_file_shell = unittest.TestSuite()
#     suite_open_file_shell.addTest(WidgetTestCase('test_open_file_shell__file_not_found'))
#     return suite_open_file_shell

# def test_read_file_suite():
#     suite_read_file = unittest.TestSuite()
#     suite_read_file.addTest(WidgetTestCase('test_read_file__not_supported'))
#     suite_read_file.addTest(WidgetTestCase('test_read_file__xlsx'))
#     return suite_read_file


# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite_open_file_gui())
#     runner.run(suite_open_file_shell())
#     runner.run(suite_read_file())
