
# Copyright (c) 2020 Alexandre Quenon - UMONS



import unittest

import greatpublicationplanner._drawer as drawer
import greatpublicationplanner._data_processor as proc
import greatpublicationplanner._file_manager as file_manager


class DrawPropertiesTest(unittest.TestCase):

    def setUp(self):
        self.properties = drawer.DrawProperties()
    

    # Test suite: editing properties - marker style
    def test_edit_marker_style__error__category_value(self):
        with self.assertRaises(ValueError):
            self.properties.edit_marker_style(category='non_existing_category')
    
    def test_edit_marker_style__error__marker_property_name(self):
        with self.assertRaises(AttributeError):
            self.properties.edit_marker_style(category='start', non_existing_property='toto')
    
    def test_edit_marker_style__error__marker_property_value(self):# FAILS because no idea how to implement the code properly
        with self.assertRaises(ValueError):
            self.properties.edit_marker_style(category='start', marker='non_existing_value')
    

    def test_edit_marker_style__pass__start_style(self):
        self.assertTrue(self.properties._marker_styles['start']['marker'] == 'o') # default
        self.properties.edit_marker_style(category='start', marker='*')
        self.assertTrue(self.properties._marker_styles['start']['marker'] == '*')
    
    def test_edit_marker_style__pass__end_style(self):
        self.assertTrue(self.properties._marker_styles['end']['marker'] == 'o') # default
        self.properties.edit_marker_style(category='end', marker='^')
        self.assertTrue(self.properties._marker_styles['end']['marker'] == '^')

    def test_edit_marker_style__pass__submission_style(self):
        self.assertTrue(self.properties._marker_styles['submission']['color'] == 'r') # default
        self.properties.edit_marker_style(category='submission', color='crimson')
        self.assertTrue(self.properties._marker_styles['submission']['color'] == 'crimson')


    def test_edit_marker_start_style__pass(self):
        self.assertTrue(self.properties._marker_styles['start']['color'] == 'k') # default
        self.properties.edit_marker_start_style(color='g')
        self.assertTrue(self.properties._marker_styles['start']['color'] == 'g')

    def test_edit_marker_end_style__pass(self):
        self.assertTrue(self.properties._marker_styles['end']['fillstyle'] == 'full') # default
        self.properties.edit_marker_end_style(fillstyle='top')
        self.assertTrue(self.properties._marker_styles['end']['fillstyle'] == 'top')

    def test_edit_marker_submission_style__pass(self):
        self.assertTrue(self.properties._marker_styles['submission']['markersize'] == 10.0) # default
        self.properties.edit_marker_submission_style(markersize=20.0)
        self.assertTrue(self.properties._marker_styles['submission']['markersize'] == 20.0)
    

    # Test suite: editing properties - timespan style
    def test_edit_timespan_style__error__category_value(self):
        with self.assertRaises(ValueError):
            self.properties.edit_timespan_style(category='non_existing_category')
    
    def test_edit_timespan_style__error__timespan_property_name(self):
        with self.assertRaises(AttributeError):
            self.properties.edit_timespan_style(category='start-end', non_existing_property='toto')
    
    def test_edit_timespan_style__error__timespan_property_value(self):# FAILS because no idea how to implement the code properly
        with self.assertRaises(ValueError):
            self.properties.edit_timespan_style(category='start-end', linestyles='non_existing_value')
    

    def test_edit_timespan_style__pass__startend_style(self):
        self.assertTrue(self.properties._timespan_styles['start-end']['linestyles'] == 'solid') # default
        self.properties.edit_timespan_style(category='start-end', linestyles='dashed')
        self.assertTrue(self.properties._timespan_styles['start-end']['linestyles'] == 'dashed')

    def test_edit_timespan_style__pass__submissionstart_style(self):
        self.assertTrue(self.properties._timespan_styles['submission-start']['colors'] == 'k') # default
        self.properties.edit_timespan_style(category='submission-start', colors='r')
        self.assertTrue(self.properties._timespan_styles['submission-start']['colors'] == 'r')


    def test_edit_timespan_startend_style__pass(self):
        self.assertTrue(self.properties._timespan_styles['start-end']['colors'] == 'k') # default
        self.properties.edit_timespan_startend_style(colors='g')
        self.assertTrue(self.properties._timespan_styles['start-end']['colors'] == 'g')

    def test_edit_timespan_submissionstart_style__pass(self):
        self.assertTrue(self.properties._timespan_styles['submission-start']['linestyles'] == 'dotted') # default
        self.properties.edit_timespan_submissionstart_style(linestyles='dashdot')
        self.assertTrue(self.properties._timespan_styles['submission-start']['linestyles'] == 'dashdot')
    

    # Test suite: draw
    def test_draw_timeline(self):
        data = file_manager.open_file_shell('./greatpublicationplanner/tests/examples/short_list_conf.csv')
        proc.make_lower_case_header(data)
        proc.convert_date_to_datetime(data)

        try:
            drawer.draw_timeline(data, self.properties)
        except:
            self.fail('An exception was thrown but not expected.')
