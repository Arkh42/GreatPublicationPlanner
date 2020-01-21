
# Copyright (c) 2020 Alexandre Quenon - UMONS



import sys

import greatpublicationplanner as gpp


planner = gpp.PlannerBatch()
file_path = "./greatpublicationplanner/tests/examples/short_list_conf.csv"
no_file_path = "./greatpublicationplanner/tests/examples/no_file.csv"

try:
    planner.load_data(file_path)
except RuntimeError:
    print(sys.exc_info())
    sys.exit('No available date')
else:
    print(planner.data)
