from actual_code.global_utils import GlobalUtils

__author__ = 'ChmHsm'

#global_file_path = GlobalUtils.latinAr_test_file
global_utils = GlobalUtils()
dataset_destination_file_path = global_utils.construct_file_url_from_parameters("Maghreb", "Morocco", "Northern -chamali", "phrases")
pre_processed_data_directory = "..\\preprocessed_data"
raw_file_path = "..\\raw_data\\lyrics\\strict_arabic"
preprocessed_file_destination = pre_processed_data_directory + "\\lyrics\\strict_arabic"

list_of_fraw_files = global_utils.filenames_from_directory(raw_file_path)
for raw_data_file in list_of_fraw_files:
    file = raw_file_path + "\\" + raw_data_file
    pre_processed_result = global_utils.pre_process_and_write_to_file(file, preprocessed_file_destination)
    print("Preprocessed data length: " + str(len(pre_processed_result)))
    new_list_of_lines = global_utils.add_list_of_words_to_dataset(pre_processed_result, dataset_destination_file_path)
    global_utils.write_json_to_file(new_list_of_lines, dataset_destination_file_path)
    print("Final data without duplicates: " + str(len(new_list_of_lines)))