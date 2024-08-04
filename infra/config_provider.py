import json


class ConfigProvider:

    @staticmethod
    def load_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                json.load(f)
        except FileNotFoundError:
            print(f"file located at:{file_path}, Is not found")
