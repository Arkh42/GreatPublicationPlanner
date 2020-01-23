# GreatPublicationPlanner

GreatPublicationPlanner is a tool to display the dates of the conferences and other publications 
you might be interested in.
Visualization will allow you to choose wisely.


## Table of contents

- [GreatPublicationPlanner for the impatients](#greatpublicationplanner-for-the-impatients)
- [Status](#status)
- [Organization of the package](#organization-of-the-package)


## GreatPublicationPlanner for the impatients


Import the package and instanciate a batch-mode planner:
```python
import greatpublicationplanner as gpp

planner = gpp.PlannerBatch()
```

Then you can load and plot data
```python
planner.load_data(path_to_file)
planner.plot_data()
```

[Tutorials](./greatpublicationplanner/tutorials) are provided inside the package.


## Status

[![License](https://img.shields.io/github/license/Arkh42/GreatPublicationPlanner?color=blue&label=License)](LICENSE)
&middot;
![Windows Build Status](https://img.shields.io/github/workflow/status/Arkh42/GreatPublicationPlanner/WIN-pythonpackage?label=Windows%20build)
&middot;
![Linux Build Status](https://img.shields.io/github/workflow/status/Arkh42/GreatPublicationPlanner/LIN-pythonpackage?label=Linux%20build)


## Organization of the package

Currently the package includes three private libraries:
1. `_file_manager.py`, whose role is to get data from permitted files;
2. `_data_processor.py`, whose role is to check data integrity and format as expected by other libraries;
3. `_drawer.py`, whose role is to draw the plots and manage the drawing properties.

All functions are tested by means of the `unittest` module.
