#from actual_code.global_utils import GlobalUtils
from actual_code.global_utils import GlobalUtils

__author__ = 'ChmHsm'

global_utils = GlobalUtils()

strict_arabic_or_latin_arabic = "strict_arabic"
dataset_destination_words_file_path = global_utils.construct_data_url_from_parameters("Maghreb", "Morocco", "Northern -chamali", "ready_data", "strict_arabic", "words")
dataset_destination_phrases_file_path = global_utils.construct_data_url_from_parameters("Maghreb", "Morocco", "Northern -chamali", "ready_data", "strict_arabic", "phrases")
pre_processed_data_directory = "..\\data\\regions\\Maghreb\\Morocco\\Northern -chamali\\preprocessed_data"
raw_files_directory = "..\\data\\regions\\Maghreb\\Morocco\\Northern -chamali\\raw_data\\lyrics\\" + strict_arabic_or_latin_arabic
preprocessed_file_destination = pre_processed_data_directory + "\\lyrics\\" + strict_arabic_or_latin_arabic


list_of_raw_files = global_utils.filenames_from_directory(raw_files_directory)
new_list_of_phrases = []
new_list_of_words = []
print("\n\nlatinAr\nDirectory: \"" + raw_files_directory + "\"")

for raw_data_file in list_of_raw_files:
    file = raw_files_directory + "\\" + raw_data_file
    print("---------------------------")
    print("Processing file: " + raw_data_file + "...")
    pre_processed_phrases_result, pre_processed_words_result = \
        global_utils.pre_process_and_write_to_file(file, preprocessed_file_destination)
    print("Preprocessed data length in file: " + str(len(pre_processed_phrases_result)))
    new_list_of_phrases, phrases_count = global_utils.add_list_of_entries_to_dataset(pre_processed_phrases_result, dataset_destination_phrases_file_path)
    new_list_of_words, words_count = global_utils.add_list_of_entries_to_dataset(pre_processed_words_result, dataset_destination_words_file_path)

    print("Number of newly added phrases to \""
          + global_utils.filename_from_file_path(dataset_destination_phrases_file_path)
          + "\": " + str(phrases_count))
    print("Number of newly added words to \""
          + global_utils.filename_from_file_path(dataset_destination_words_file_path)
          + "\": " + str(words_count))

    global_utils.write_json_to_file(new_list_of_phrases, dataset_destination_phrases_file_path)
    global_utils.write_json_to_file(new_list_of_words, dataset_destination_words_file_path)

print("\n##################################")
print("Final data in \"" + global_utils.filename_from_file_path(dataset_destination_phrases_file_path)
      + "\" without duplicates: " + str(len(new_list_of_phrases)))
print("Final data in \"" + global_utils.filename_from_file_path(dataset_destination_words_file_path)
      + "\" without duplicates: " + str(len(new_list_of_words)))
