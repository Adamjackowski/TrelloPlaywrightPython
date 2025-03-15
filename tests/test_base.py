"""Base Test Module"""
from pathlib import Path
import json
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)


class TestBase:
    """Base Test Class"""
    @staticmethod
    def data():
        """Method for opening json file"""
        with open(file=Path(f"{currentdir}/config.json"),
                  mode="r+",
                  encoding="utf-8") as config_file:
            data = json.load(config_file)
            config_file.close()
        return data

    @staticmethod
    def update_data(key, value):
        """Method for updating json file"""
        with open(file=Path(f"{currentdir}/config.json"),
                  mode="r+",
                  encoding="utf-8" ) as config_file:
            data = json.load(config_file)
            data[key] = value
            config_file.seek(0)
            json.dump(data, config_file, indent=4)
            config_file.truncate()
        return True
