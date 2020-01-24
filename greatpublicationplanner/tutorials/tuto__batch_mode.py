
# Copyright (c) 2020 Alexandre Quenon - UMONS



import sys

import greatpublicationplanner as gpp


planner = gpp.PlannerBatch()
planner.USE_ABBREV = True # default is true

file_path = "./greatpublicationplanner/tests/examples/short_list_conf.csv"
no_file_path = "./greatpublicationplanner/tests/examples/no_file.csv"

try:
    planner.load_data(file_path)
except RuntimeError:
    print(sys.exc_info())
    sys.exit('No available date')
else:
    print(planner.data)
    planner.draw_properties.edit_marker_start_style(color='g')
    planner.draw_properties.edit_marker_end_style(color='b')
    planner.draw_properties.edit_marker_submission_style(marker='X')
    planner.plot_data()
