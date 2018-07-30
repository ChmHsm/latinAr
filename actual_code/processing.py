#from actual_code.global_utils import GlobalUtils
from actual_code.global_utils import GlobalUtils

__author__ = 'ChmHsm'

global_utils = GlobalUtils()

strict_arabic_or_latin_arabic = "strict_arabic"
dataset_destination_file_path = global_utils.construct_data_url_from_parameters("Maghreb", "Morocco", "Northern -chamali", "phrases")
pre_processed_data_directory = "..\\data\\regions\\Maghreb\\Morocco\\Northern -chamali\\preprocessed_data"
raw_files_directory = "..\\data\\regions\\Maghreb\\Morocco\\Northern -chamali\\raw_data\\lyrics\\" + strict_arabic_or_latin_arabic
preprocessed_file_destination = pre_processed_data_directory + "\\lyrics\\" + strict_arabic_or_latin_arabic


list_of_raw_files = global_utils.filenames_from_directory(raw_files_directory)
new_list_of_lines = []
print("\n\nlatinAr\nDirectory: \"" + raw_files_directory + "\"")

for raw_data_file in list_of_raw_files:
    file = raw_files_directory + "\\" + raw_data_file
    print("---------------------------")
    print("Processing file: " + raw_data_file + "...")
    pre_processed_result = global_utils.pre_process_and_write_to_file(file, preprocessed_file_destination)
    print("Preprocessed data length in file: " + str(len(pre_processed_result)))
    new_list_of_lines, count = global_utils.add_list_of_words_to_dataset(pre_processed_result, dataset_destination_file_path)
    print("Number of newly added data entries to \""
          + global_utils.filename_from_file_path(dataset_destination_file_path)
          + "\": " + str(count))
    global_utils.write_json_to_file(new_list_of_lines, dataset_destination_file_path)

print("\n##################################")
print("Final data in \"" + global_utils.filename_from_file_path(dataset_destination_file_path)
      + "\" without duplicates: " + str(len(new_list_of_lines)))
