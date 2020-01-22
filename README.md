# GreatPublicationPlanner
Planning publication is sometimes a brain-teaser. The GreatPublicationPlanner gives you a tool to display the dates the conferences and other publications you might be interested in, and then to allow you to choose wisely.


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


## Organization of the package
Currently the package includes three private libraries:
1. `_file_manager.py`, whose role is to get data from permitted files;
2. `_data_processor.py`, whose role is to check data integrity and format as expected by other libraries;
3. `_drawer.py`, whose role is to draw the plots and manage the drawing properties.

All functions are tested by means of the `unittest` module.
