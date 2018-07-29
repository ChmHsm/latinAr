__author__ = 'ChmHsm'

import json
import os
import re
from os import listdir
from os.path import isfile, join


class GlobalUtils:
    regexp_file_path = "..\\raw_data\\regular_expressions"
    #latinAr_test_file = "..\\raw_data\\lyrics\\strict_arabic\\Muslim - Dommini.txt"


    @staticmethod
    def get_regexp(regexp_name):
        with open(GlobalUtils.regexp_file_path) as f:
            data = json.load(f)
            if data[regexp_name] != "":
                return data[regexp_name]
            return ""

    #parameters methods have to strictly respect project hierarchy (with cases) in the dataset directory
    @staticmethod
    def construct_file_url_from_parameters(region, country, country_region, data_type):
        return "..\\dataset\\regions\\" + region + "\\" + country + "\\" + country_region + "\\" + data_type

    @staticmethod
    def load_lines_from_json_file(json_file_path):
        with open(json_file_path, encoding="utf-16") as f:
            data = json.load(f)
            return data

    @staticmethod
    def add_list_of_words_to_dataset(list_of_words, csv_file_path):
        lines = GlobalUtils.load_lines_from_json_file(csv_file_path)
        list_of_existing_lines = []
        for line in lines:
            for inner_line in line["latin_ar"]:
                if not list_of_existing_lines.__contains__(inner_line):
                    list_of_existing_lines.append(inner_line)

        for line in list_of_words:
            if not list_of_existing_lines.__contains__(line[0]):
                list_of_existing_lines.append(line[0])
                lines.append({"latin_ar": line, "classical_arabic":""})

        return lines

    @staticmethod
    def write_json_to_file(json_data, file_path):
        GlobalUtils.delete_file_if_exists(file_path)
        lines = json.dumps(json_data,ensure_ascii=False, indent=4)
        with open(file_path, 'x', encoding="utf-16") as outfile:
            outfile.write(lines)

    @staticmethod
    def delete_file_if_exists(file_path_to_delete):
        if os.path.exists(file_path_to_delete):
            os.remove(file_path_to_delete)

    @staticmethod
    def import_raw_file(file_path):
        if file_path == "":
            return []
        else:
            with open(file_path, encoding="utf-16le") as f:
                content = f.readlines()
                list_of_lines = []
                for x in content:
                    if x.strip() == "":
                        continue
                    else:
                        list_of_lines.append(x.strip())
                return list_of_lines

    @staticmethod
    def pre_process_and_write_to_file(raw_file_path, preprocessed_destination_directory):
        list_of_file_lines = GlobalUtils.import_raw_file(raw_file_path)
        tmp_list = []
        destination_file_path = preprocessed_destination_directory + "\\" + GlobalUtils.filename_from_file_path(raw_file_path)
        GlobalUtils.delete_file_if_exists(destination_file_path)
        with open(destination_file_path, "x", encoding="utf-16") as f:
            for tmpLine in list_of_file_lines:
                tmp_matched = re.findall(
                    GlobalUtils.get_regexp("arabic_letters_with_chakl_and_numbers_and_arabic_punctuation"),
                    tmpLine)
                if tmp_matched:
                    tmp_list.append(tmp_matched)
                    f.write(tmp_matched[0]+"\n")
            return tmp_list

    @staticmethod
    def filename_from_file_path(file_path):
        split_file_path = file_path.split("\\")
        return split_file_path[-1]

    @staticmethod
    def filenames_from_directory(directory):
        onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
        return onlyfiles
