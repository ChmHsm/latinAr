import re

__author__ = 'ChmHsm'
global_file_path = "..\\raw_data\\lyrics\\strict_arabic\\Muslim - 3ayn l7amra.txt"

# Match characters written in arabic letters, strip latin chars and special chars except punctuation:
# i.e.: .حيت هو حقّار، الحبس ولّا القبر
strict_arabic_regexp = r'[^\w]'

# TODO write regexp to match strings written in french or english arabic,
# but strip strict arabic and special chars except numbers from 0 to 9 and punctuation
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


def pre_process_and_write_to_file():
    list_of_file_lines = import_raw_file(global_file_path)
    tmp_list = []
    for tmpLine in list_of_file_lines:
        tmp_list.append(re.sub(strict_arabic_regexp, ' ', tmpLine))
    return tmp_list


pre_processed_result = pre_process_and_write_to_file()
for line in pre_processed_result:
    print(line)
