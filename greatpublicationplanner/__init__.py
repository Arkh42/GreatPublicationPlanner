
# Copyright (c) 2020 Alexandre Quenon - UMONS



import greatpublicationplanner._file_manager as file_manager
import greatpublicationplanner._data_processor as proc
import greatpublicationplanner._drawer as drawer


class PlannerBatch:
    """
    Planner for batch-mode operations.
    """

    def __init__(self):
        self.graphic_properties = drawer.DrawProperties()
        self.data = None

    def load_data(self, file_path):
        try:
            self.data = file_manager.open_file_shell(file_path)
            proc.make_lower_case_header(self.data)
            proc.check_data_integrity(self.data)
        except (FileNotFoundError, ValueError) as error_message:
            raise RuntimeError('Error while loading the file: {}'.format(error_message))
        except KeyError as error_message:
            raise RuntimeError('Corrupted data: {}'.format(error_message))
        except:
            raise RuntimeError('Unexpected error!')


class PlannerGUI:
    """
    Planner for GUI-mode operations.
    """

    pass
