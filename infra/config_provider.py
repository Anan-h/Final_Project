import json
import os


class ConfigProvider:

    @staticmethod
    def load_from_file(file_name):
        """
        a function to read an external file
        :param file_name: the path of the file
        :return: reading the data
        """
        try:
            absolute_path = os.path.abspath(file_name)
            with open(absolute_path, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print(f"File {file_name} is not found")


