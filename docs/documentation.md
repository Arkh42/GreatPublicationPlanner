---
layout: default
title: Documentation
---


Contents:
- [Quick start](#quick-start)
- [Package organization](#package-organization)



# Quick start

Import the package and instantiate a batch-mode planner:
```python
import greatpublicationplanner as gpp

planner = gpp.PlannerBatch()
```

Then you can load and plot data with
```python
planner.load_data(path_to_file)
planner.plot_data()
```
and that's it!



# Package organization

The package is organized as follows:
- three 'weak' private modules that are not supposed to be accessed directly by the user
	1. `_file_manager.py`, whose role is to get/dump data from/to permitted files;
	2. `_data_processor.py`, whose role is to check data integrity and format as expected by other libraries;
	3. `_drawer.py`, whose role is to draw the plots and manage the drawing properties;
- `__init__`, which defines the main planner classes that are instantiated by user.


## Planner classes

Currently, only one class is available: `PlannerBatch`, which creates a planner for batch-mode operations,
i.e., no GUI except for showing the resulting plot.

A `PlannerGUI` class is planned to allow the user to create a planner with some GUI interactivity,
but not implemented yet.


## Testing

The code is tested by means of the `unittest` module.

A GitHub workflow is implemented on the `master` branch and tests the following configurations:
- OS = [Windows];
- python-version = [3.5, 3.6, 3.7].

The aim is to be OS-independent and to work properly with Python 3.x.


[back](./)
