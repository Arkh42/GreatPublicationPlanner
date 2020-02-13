
# Copyright (c) 2020 Alexandre Quenon - UMONS

"""
Draw the graphics to display the information about publications.
"""


from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as dt
from matplotlib.colors import is_color_like
from pandas import to_datetime
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


class DrawProperties:
    """
    Embeds properties used for drawings and methods to modify them properly.
    """

    def __init__(self):
        self.__available_marker_properties = {
            'marker':self.__is_available_marker,
            'fillstyle':self.__is_available_fillstyle,
            'color':self.__is_available_color,
            'markersize':self.__is_available_size
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
            'linestyles':self.__is_available_linestyles,
            'colors':self.__is_available_color
        }
        self._timespan_startend_style = {'linestyles':'solid', 'colors':'k'}
        self._timespan_submissionstart_style = {'linestyles':'dotted', 'colors':'k'}
        self._timespan_styles = {
            'start-end':self._timespan_startend_style,
            'submission-start':self._timespan_submissionstart_style
        }

        self.__available_today_properties = {
            'linestyle':self.__is_available_linestyle,
            'color':self.__is_available_color,
            'linewidth':self.__is_available_size
        }
        self._today_style = {'linestyle':'-', 'linewidth':'2', 'color':'r'}

        self._display_legend = True


    # Callbacks for value testing
    def __is_available_marker(self, marker): # Matplotlib 3.1.1
        return marker in ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
    
    def __is_available_fillstyle(self, style): # Matplotlib 3.1.1
        return style in ('full', 'left', 'right', 'bottom', 'top', 'none')
    
    def __is_available_color(self, color):
        return is_color_like(color)
    
    def __is_available_size(self, size):
        try:
            size = float(size)
        except ValueError:
            return False
        else:
            if size > 0.0:
                return True
            else:
                return False

    def __is_available_linestyle(self, style):
        return style in ('-', '--', '-.', ':')

    def __is_available_linestyles(self, style):
        return style in ('solid', 'dashed', 'dashdot', 'dotted')


    # Low-level interface
    def edit_marker_style(self, category, **marker_properties):
        if category in self._marker_styles.keys():
            if all(feature in self.__available_marker_properties.keys() for feature in marker_properties.keys()):
                if all(map(lambda x: self.__available_marker_properties[x](marker_properties[x]), marker_properties.keys())):
                    self._marker_styles[category].update(marker_properties)
                else:
                    raise ValueError('Forbidden value passed to a marker property.')
            else:
                raise AttributeError('Properties can be {}.'.format(self.__available_marker_properties.keys()))
        else:
            raise ValueError('The category argument must be {}.'.format(self._marker_styles.keys()))
    
    def edit_timespan_style(self, category, **timespan_properties):
        if category in self._timespan_styles.keys():
            if all(feature in self.__available_timespan_properties.keys() for feature in timespan_properties.keys()):
                if all(map(lambda x: self.__available_timespan_properties[x](timespan_properties[x]), timespan_properties.keys())):
                    self._timespan_styles[category].update(timespan_properties)
                else:
                    raise ValueError('Forbidden value passed to a timespan property.')
            else:
                raise AttributeError('Properties can be {}.'.format(self.__available_timespan_properties.keys()))
        else:
            raise ValueError('The category argument must be {}.'.format(self._timespan_styles.keys()))
    
    def edit_today_style(self, **today_properties):
        if all(feature in self.__available_today_properties.keys() for feature in today_properties.keys()):
            if all(map(lambda x: self.__available_today_properties[x](today_properties[x]), today_properties.keys())):
                self._today_style.update(today_properties)
            else:
                raise ValueError('Forbidden value passed to a today property.')
        else:
            raise AttributeError('Properties can be {}.'.format(self.__available_today_properties.keys()))


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


    def show_legend(self):
        self._display_legend = True
    
    def hide_legend(self):
        self._display_legend = False


def draw_timeline(data, draw_properties, use_abbreviations=True):
    # Prepare figure and common axes
    fig, ax = plt.subplots(1, 1)

    # Define the position of labels on y axis for compactness
    ylocs = [i*0.2 for i in range(len(data.name))]
    ax.set_yticks(ylocs)
    local_data = data.assign(ylocs=ylocs)

    if use_abbreviations:
        ax.set_yticklabels(data.abbreviation.fillna(data.name))
    else:
        ax.set_yticklabels(data.name)

    # Plot the data
    ax.xaxis_date()
    ax.hlines(ylocs, dt.date2num(data.start), dt.date2num(data.end), **draw_properties._timespan_startend_style)
    marker_start = ax.plot(dt.date2num(data.start), ylocs, linestyle='None', **draw_properties._marker_start_style)
    marker_end = ax.plot(dt.date2num(data.end), ylocs, linestyle='None', **draw_properties._marker_end_style)
    ax.hlines(ylocs, dt.date2num(data.submission), dt.date2num(data.start), **draw_properties._timespan_submissionstart_style)
    marker_submission = ax.plot(dt.date2num(data.submission), ylocs, linestyle='None', **draw_properties._marker_submission_style)

    # Format x axis
    ax.xaxis.set_major_locator(dt.MonthLocator())
    ax.xaxis.set_major_formatter(dt.DateFormatter('%b\n%Y'))

    # Revert y axis for display in chronological order
    ax.invert_yaxis()

    # Display grid as dotted
    ax.grid(linestyle=':')

    # Display days under markers
    for _, row in local_data.dropna(subset=['submission']).iterrows():
        plt.text(dt.date2num(row['submission']), row['ylocs']+0.01, row['submission'].day, horizontalalignment='center', verticalalignment='top')
    for _, row in local_data.dropna(subset=['start']).iterrows():
        plt.text(dt.date2num(row['start']), row['ylocs']+0.01, row['start'].day, horizontalalignment='right', verticalalignment='top')
    for _, row in local_data.dropna(subset=['end']).iterrows():
        plt.text(dt.date2num(row['end']), row['ylocs']+0.01, row['end'].day, horizontalalignment='left', verticalalignment='top')

    # Display locations
    for _, row in local_data.dropna(subset=['start']).iterrows():
        plt.text(dt.date2num(row['start']), row['ylocs'], row['location'], verticalalignment='bottom')

    # Display legend
    if draw_properties._display_legend:
        ax.legend(['Start', 'End', 'Submission'])

    return fig, ax


def plot_today_on(ax, draw_properties):
    date = datetime.today().strftime('%Y-%m-%d')
    date = to_datetime(date)

    ax.axvline(date, **draw_properties._today_style)
    plt.text(date, ax.get_ylim()[1], 'Today', color=draw_properties._today_style['color'], horizontalalignment='center', verticalalignment='bottom')
