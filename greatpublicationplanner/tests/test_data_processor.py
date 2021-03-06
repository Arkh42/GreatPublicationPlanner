
# Copyright (c) 2020 Alexandre Quenon - UMONS



import unittest

import pandas as pd

import greatpublicationplanner._data_processor as processor
import greatpublicationplanner._file_manager as file_manager


class DataProcessorTest(unittest.TestCase):

    def setUp(self):
        self.data_raw = file_manager.open_file_shell('./greatpublicationplanner/tests/examples/short_list_conf.csv')
        self.data_ok = file_manager.open_file_shell('./greatpublicationplanner/tests/examples/short_list_conf.csv')
        processor.make_lower_case_header(self.data_ok)


    # Test suite: data format
    def test_make_lower_case_header(self):
        processor.make_lower_case_header(self.data_raw)
        for header in self.data_raw:
            self.assertTrue(header.islower())
    
    def test_convert_date_to_datetime(self):
        self.assertTrue(isinstance(self.data_ok['start'][0], str))
        self.assertTrue(isinstance(self.data_ok['end'][0], str))
        self.assertTrue(isinstance(self.data_ok['submission'][0], str))
        processor.convert_date_to_datetime(self.data_ok)
        self.assertTrue(isinstance(self.data_ok['start'][0], pd.Timestamp))
        self.assertTrue(isinstance(self.data_ok['end'][0], pd.Timestamp))
        self.assertTrue(isinstance(self.data_ok['submission'][0], pd.Timestamp))
    

    # Test suite: data integrity
    def test_has_name__false(self):
        data_corrupted = self.data_ok.rename(columns={'name':'toto'})
        self.assertFalse(processor.has_name(data_corrupted))

    def test_has_name__true(self):
        self.assertTrue(processor.has_name(self.data_ok))
    

    def test_has_abbreviation__false(self):
        data_corrupted = self.data_ok.rename(columns={'abbreviation':'toto'})
        self.assertFalse(processor.has_abbreviation(data_corrupted))

    def test_has_abbreviation__true(self):
        self.assertTrue(processor.has_abbreviation(self.data_ok))


    def test_has_start_date__false(self):
        data_corrupted = self.data_ok.rename(columns={'start':'toto'})
        self.assertFalse(processor.has_start_date(data_corrupted))

    def test_has_start_date__true(self):
        self.assertTrue(processor.has_start_date(self.data_ok))
    

    def test_has_end_date__false(self):
        data_corrupted = self.data_ok.rename(columns={'end':'toto'})
        self.assertFalse(processor.has_end_date(data_corrupted))

    def test_has_end_date__true(self):
        self.assertTrue(processor.has_end_date(self.data_ok))
    

    def test_has_submission_date__false(self):
        data_corrupted = self.data_ok.rename(columns={'submission':'toto'})
        self.assertFalse(processor.has_submission_date(data_corrupted))

    def test_has_submission_date__true(self):
        self.assertTrue(processor.has_submission_date(self.data_ok))
    

    def test_check_data_integrity__missing_name(self):
        data_corrupted = self.data_ok.rename(columns={'name':'toto'})
        with self.assertRaises(KeyError):
            processor.check_data_integrity(data_corrupted)
    
    def test_check_data_integrity__missing_abbreviation(self):
        data_corrupted = self.data_ok.rename(columns={'abbreviation':'toto'})
        with self.assertRaises(KeyError):
            processor.check_data_integrity(data_corrupted)
    
    def test_check_data_integrity__missing_start_date(self):
        data_corrupted = self.data_ok.rename(columns={'start':'toto'})
        with self.assertRaises(KeyError):
            processor.check_data_integrity(data_corrupted)
    
    def test_check_data_integrity__missing_end_date(self):
        data_corrupted = self.data_ok.rename(columns={'end':'toto'})
        with self.assertRaises(KeyError):
            processor.check_data_integrity(data_corrupted)
    
    def test_check_data_integrity__missing_submission_date(self):
        data_corrupted = self.data_ok.rename(columns={'submission':'toto'})
        with self.assertRaises(KeyError):
            processor.check_data_integrity(data_corrupted)
    
    def test_check_data_integrity__ok(self):
        try:
            processor.check_data_integrity(self.data_ok)
        except KeyError:
            self.fail('An exception was thrown but not expected.')
    

    # Test suite: sort
    def test_sort_on_name__ascending(self):
        processor.sort_on_name(self.data_ok, ascending=True)
        self.assertTrue(self.data_ok.name.is_monotonic_increasing)
    
    def test_sort_on_name__descending(self):
        processor.sort_on_name(self.data_ok, ascending=False)
        self.assertTrue(self.data_ok.name.is_monotonic_decreasing)
    

    def test_sort_on_submission__ascending(self):
        processor.sort_on_submission(self.data_ok, ascending=True)
        self.assertTrue(self.data_ok.submission.is_monotonic_increasing)
    
    def test_sort_on_submission__descending(self):
        processor.sort_on_submission(self.data_ok, ascending=False)
        self.assertTrue(self.data_ok.submission.is_monotonic_decreasing)
    

    def test_sort_on_start__ascending(self):
        processor.sort_on_start(self.data_ok, ascending=True)
        self.assertTrue(self.data_ok.start.is_monotonic_increasing)
    
    def test_sort_on_start__descending(self):
        processor.sort_on_start(self.data_ok, ascending=False)
        self.assertTrue(self.data_ok.start.is_monotonic_decreasing)
    

    def test_sort_on_end__ascending(self):
        processor.sort_on_end(self.data_ok, ascending=True)
        self.assertTrue(self.data_ok.end.is_monotonic_increasing)
    
    def test_sort_on_end__descending(self):
        processor.sort_on_end(self.data_ok, ascending=False)
        self.assertTrue(self.data_ok.end.is_monotonic_decreasing)
