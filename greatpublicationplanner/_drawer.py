
# Copyright (c) 2020 Alexandre Quenon - UMONS

"""
Draw the graphics to display the information about publications.
"""


from matplotlib import pyplot as plt
from matplotlib import dates as dt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


class DrawProperties:
    """
    Embeds properties used for drawings and methods to modify them properly.
    """

    def __init__(self):
        self.__available_marker_properties = { # Matplotlib 3.1.1
            'marker':('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X'),
            'fillstyle':('full', 'left', 'right', 'bottom', 'top', 'none'),
            'color':'',# not defined because too many possibilities
            'markersize':''# not defined because too many possibilities (positive real number)
        }
        self._marker_start_style = {'marker':'o', 'markersize':5.0, 'color':'k', 'fillstyle':'full'}
        self._marker_end_style = self._marker_start_style.copy()
        self._marker_submission_style = {'marker':'o', 'markersize':10.0, 'color':'r', 'fillstyle':'full'}
        self._marker_styles = {
            'start':self._marker_start_style,
            'end':self._marker_end_style,
            'submission':self._marker_submission_style
        }
        
        self.__available_timespan_properties = { # Matplotlib 3.1.1
            'linestyles':('solid', 'dashed', 'dashdot', 'dotted'),
            'colors':''# not defined because too many possibilities
        }
        self._timespan_startend_style = {'linestyles':'solid', 'colors':'k'}
        self._timespan_submissionstart_style = {'linestyles':'dotted', 'colors':'k'}
        self._timespan_styles = {
            'start-end':self._timespan_startend_style,
            'submission-start':self._timespan_submissionstart_style
        }

    
    # Low-level interface
    def edit_marker_style(self, category, **marker_properties):
        if category in self._marker_styles.keys():
            if all(feature in self.__available_marker_properties.keys() for feature in marker_properties.keys()):
                self._marker_styles[category].update(marker_properties)
            else:
                raise AttributeError('Properties can be {}.'.format(self.__available_marker_properties.keys()))
        else:
            raise ValueError('The category argument must be {}.'.format(self._marker_styles.keys()))
    
    def edit_timespan_style(self, category, **timespan_properties):
        if category in self._timespan_styles.keys():
            if all(feature in self.__available_timespan_properties.keys() for feature in timespan_properties.keys()):
                self._timespan_styles[category].update(timespan_properties)
            else:
                raise AttributeError('Properties can be {}.'.format(self.__available_timespan_properties.keys()))
        else:
            raise ValueError('The category argument must be {}.'.format(self._timespan_styles.keys()))
    

    # High-level interface
    def edit_marker_start_style(self, **marker_properties):
        self.edit_marker_style(category='start', **marker_properties)
    
    def edit_marker_end_style(self, **marker_properties):
        self.edit_marker_style(category='end', **marker_properties)
    
    def edit_marker_submission_style(self, **marker_properties):
        self.edit_marker_style(category='submission', **marker_properties)
    
    def edit_timespan_startend_style(self, **timespan_properties):
        self.edit_timespan_style(category='start-end', **timespan_properties)
    
    def edit_timespan_submissionstart_style(self, **timespan_properties):
        self.edit_timespan_style(category='submission-start', **timespan_properties)


def draw_timeline(data, draw_properties):
    # Prepare figure and common axes
    fig, ax = plt.subplots(1, 1)

    # Define the position of labels on y axis for compactness
    ylocs = [i*0.2 for i in range(len(data.name))]
    ax.set_yticks(ylocs)
    ax.set_yticklabels(data.name)

    # Plot the data
    ax.xaxis_date()
    ax.hlines(ylocs, dt.date2num(data.start), dt.date2num(data.end), **draw_properties._timespan_startend_style)
    ax.plot(dt.date2num(data.start), ylocs, linestyle='None', **draw_properties._marker_start_style)
    ax.plot(dt.date2num(data.end), ylocs, linestyle='None', **draw_properties._marker_end_style)
    ax.hlines(ylocs, dt.date2num(data.submission), dt.date2num(data.start), **draw_properties._timespan_submissionstart_style)
    ax.plot(dt.date2num(data.submission), ylocs, linestyle='None', **draw_properties._marker_submission_style)

    # Display timeline per week (x axis)
    rule = dt.rrulewrapper(dt.WEEKLY, interval=1)
    loc = dt.RRuleLocator(rule)
    ax.xaxis.set_major_locator(loc)

    # Date format (x axis)
    formatter = dt.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(formatter)

    # Rotate and align the tick labels so they look better
    fig.autofmt_xdate()

    # Revert y axis for display in chronological order
    ax.invert_yaxis()

    # Display grid as dotted
    ax.grid(linestyle = ':')

    return fig, ax