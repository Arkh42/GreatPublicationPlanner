
# Copyright (c) 2020 Alexandre Quenon - UMONS



import unittest

import greatpublicationplanner as gpp


class PlannerBatchTest(unittest.TestCase, gpp.PlannerBatch):

    def setUp(self):
        self.path__no_file = './greatpublicationplanner/tests/examples/no_file.csv'
        self.path__file_not_supported = './greatpublicationplanner/tests/examples/list_conf.toto'
        self.path__file_corrupted = './greatpublicationplanner/tests/examples/short_list_conf_corrupted.csv'
        self.path__data_ok = './greatpublicationplanner/tests/examples/short_list_conf.csv'
    

    #Test suite: loading data
    def test_load_data__error__no_file(self):
        with self.assertRaises(RuntimeError):
            self.load_data(self.path__no_file)
    
    def test_load_data__error__unsupported_file(self):
        with self.assertRaises(RuntimeError):
            self.load_data(self.path__file_not_supported)
    
    def test_load_data__error__corrupted_file(self):
        with self.assertRaises(RuntimeError):
            self.load_data(self.path__file_corrupted)
    
    def test_load_data__pass(self):
        try:
            self.load_data(self.path__data_ok)
        except:
            self.fail('Unpected exception.')
