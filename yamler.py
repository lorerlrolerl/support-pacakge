"""
This module contains functions to handle yaml files
"""
import yaml


def read_yaml(file_path, settings=None):
    """
    Reads a yaml file and returns a dictionary
    In case we want a specific settings from the yaml file, we can pass it as a parameter
    """
    with open(file_path, "r", encoding="utf-8") as file:
        file = yaml.load(file, Loader=yaml.FullLoader)
        if settings:
            return file[settings]
        return file
