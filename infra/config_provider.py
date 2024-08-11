import json
import os


class ConfigProvider:

    @staticmethod
    def load_from_file(file_path, current_path):
        base_dir = os.path.dirname(os.path.abspath(current_path))
        full_path = os.path.join(base_dir, file_path)
        try:
            with open(full_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
