import json
import os
import re
from os import listdir
from os.path import isfile, join

__author__ = 'ChmHsm'

regexp_file_path = "..\\data\\regions\\Maghreb\\Morocco\\regular_expressions"
regex_between_parentheses = r'\([^)]*\)'
regex_between_brackets = r'\[[^]]*\]'

class GlobalUtils:

    @staticmethod
    def get_regexp(regexp_name):
        with open(regexp_file_path, encoding="utf-16") as f:
            data = json.load(f)
            if data[regexp_name] != "":
                return data[regexp_name]
            return ""

    #parameters methods have to strictly respect project hierarchy (with cases) in the data directory
    @staticmethod
    def construct_data_url_from_parameters(*args):
        directory_result = ""
        for directory in args:
            directory_result += directory + "\\"
        return "..\\data\\regions\\" + directory_result.strip("\\")
        # return "..\\data\\regions\\" + region + "\\" + country + "\\" + country_region + "\\" + data_type

    @staticmethod
    def load_lines_from_json_file(json_file_path):
        with open(json_file_path, encoding="utf-16") as f:
            data = json.load(f)
            return data

    @staticmethod
    def add_list_of_entries_to_dataset(list_of_entries, csv_file_path):
        lines = GlobalUtils.load_lines_from_json_file(csv_file_path)
        list_of_existing_lines = []
        for line in lines:
            for inner_line in line["latin_ar"]:
                if not list_of_existing_lines.__contains__(inner_line):
                    list_of_existing_lines.append(inner_line)
        count = 0
        for line in list_of_entries:
            if not list_of_existing_lines.__contains__(line):
                count += 1
                list_of_existing_lines.append(line)
                lines.append({"latin_ar": [line], "classical_arabic":""})

        return lines, count

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
    def pre_process_and_write_to_file(raw_file_path, preprocessed_destination_directory, regex_name,
                                      remove_between_parentheses = False, remove_between_brackets = False):
        list_of_file_lines = GlobalUtils.import_raw_file(raw_file_path)
        tmp_phrases_list = []
        tmp_words_list = []
        destination_file_path = preprocessed_destination_directory + "\\" + GlobalUtils.filename_from_file_path(raw_file_path)
        GlobalUtils.delete_file_if_exists(destination_file_path)
        with open(destination_file_path, "x", encoding="utf-16") as f:
            for tmpLine in list_of_file_lines:
                tmp_parentheses_brackets = tmpLine
                if remove_between_parentheses:
                    tmp_parentheses_brackets = re.sub(regex_between_parentheses, '', tmp_parentheses_brackets)
                if remove_between_brackets:
                    tmp_parentheses_brackets = re.sub(regex_between_brackets, '', tmp_parentheses_brackets)
                if len(tmp_parentheses_brackets.strip()) > 0:
                    tmp_matched = re.findall(
                        GlobalUtils.get_regexp(regex_name),
                        tmp_parentheses_brackets)
                    if tmp_matched:
                        for word in tmp_matched[0].split(" "):
                            tmp_words_list.append(word.strip())
                        if tmp_matched[0].strip() != '':
                            tmp_phrases_list.append(tmp_matched[0].strip())
                            f.write(tmp_matched[0]+"\n")
            return tmp_phrases_list, tmp_words_list

    @staticmethod
    def filename_from_file_path(file_path):
        split_file_path = file_path.split("\\")
        return split_file_path[-1]

    @staticmethod
    def filenames_from_directory(directory):
        onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
        return onlyfiles