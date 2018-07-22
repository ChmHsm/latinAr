__author__ = 'ChmHsm'

import json


class GlobalUtils:
    regexp_file_path = "..\\raw_data\\regular_expressions"
    latinAr_test_file = "..\\raw_data\\lyrics\\strict_arabic\\Muslim - 3ayn l7amra.txt"
    pre_processed_data_directory = "..\\preprocessed_data"

    def get_regexp(self, regexp_name):
        with open(self.regexp_file_path) as f:
            data = json.load(f)
            if data[regexp_name] != "":
                return data[regexp_name]
            return ""
