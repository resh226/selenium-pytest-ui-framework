"""
file_utils.py
==============

This module provides utility functions for file operations within the automation framework.

Currently, it contains a helper class `FileUtils` with methods for reading JSON files.
Centralizing file operations ensures consistent error handling and improves maintainability.

Typical usage:
--------------
from utils.file_utils import FileUtils

config = FileUtils.read_json('config.json')
test_data = FileUtils.read_json('test_data/basic_cases.json')
test_data = FileUtils.read_json('test_data/basic_cases.json')
test_data = FileUtils.read_json('test_data/flow_cases.json')
"""

import json
import os


class FileUtils:
    @staticmethod
    def read_json(file_path):
        """
        Reads a JSON file and returns its content as a Python dictionary.

        :param file_path: Path to the JSON file.
        :return: Dictionary with JSON data.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not valid JSON.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
