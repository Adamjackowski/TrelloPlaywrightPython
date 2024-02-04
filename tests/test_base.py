import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
import pytest
import json
from datetime import datetime
import json
from pathlib import Path

class TestBase:
        
    @staticmethod
    def data():
        with open(Path(f"{currentdir}/config.json"),"r+") as config_file:
            data = json.load(config_file)
            config_file.close()
        return data

    @staticmethod
    def update_data(key, value):
        with open(Path(f"{currentdir}/config.json"),"r+") as config_file:
            data = json.load(config_file)
            data[key] = value
            config_file.seek(0)
            json.dump(data, config_file, indent=4)
            config_file.truncate()
        return True
        