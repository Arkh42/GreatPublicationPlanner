# GreatPublicationPlanner
Planning publication is sometimes a brain-teaser. The GreatPublicationPlanner gives you a tool to display the dates the conferences and other publications you might be interested in, and then to allow you to choose wisely.


## Organization of the package
Currently the package includes two private libraries:
1. `_file_manager.py`, whose role is to get data from permitted files;
2. `_data_processor.py`, whose role is to check data integrity and format as expected by other libraries.

All functions are tested by means of the `unittest` module.
