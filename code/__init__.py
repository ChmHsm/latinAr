__author__ = 'ChmHsm'

import re
import os

from code.global_utils import GlobalUtils

global_file_path = GlobalUtils.latinAr_test_file
global_utils = GlobalUtils()

# TODO write regexp to match strings written in latin arabic:
# strictly match latin chars and numbers from 0 to 9 and punctuation
# remove special chars except punctuation
# Remove EVERYTHING in parentheses (), brackets [], and curly brackets {}
# i.e.: 3chiri 3ayno 7amra, 9elbo cha3el jamra
latin_arabic_regexp = r''


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


def filename_from_file_path(file_path):
    split_file_path = file_path.split("\\")
    return split_file_path[-1]


def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def pre_process_and_write_to_file():
    list_of_file_lines = import_raw_file(global_file_path)
    tmp_list = []
    destination_file_path = global_utils.pre_processed_data_directory + "\\lyrics\\strict_arabic\\" + \
                            filename_from_file_path(global_file_path)
    delete_file_if_exists(destination_file_path)
    # TODO new written file has unexpected content (probably encoding)
    f = open(destination_file_path, "x", encoding="utf-16le")
    for tmpLine in list_of_file_lines:
        tmp_matched = re.findall(
            global_utils.get_regexp("arabic_letters_with_chakl_and_numbers_and_arabic_punctuation"),
            tmpLine)
        if tmp_matched:
            tmp_list.append(tmp_matched)
            f.write(tmp_matched[0])
    return tmp_list


pre_processed_result = pre_process_and_write_to_file()
for line in pre_processed_result:
    print(line[0])
