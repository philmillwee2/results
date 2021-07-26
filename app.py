import pprint
from results import process

pp = pprint.PrettyPrinter(indent=4)

RESULTS_TO_PROCESS_PATH = "./data/original"
RESULTS_CONVERTED_PATH = "./data/converted"

def get_converted_results_path(path):
    output_dir = RESULTS_CONVERTED_PATH
    return output_dir + "/" + path.split("/")[-1]

results_file_list = process.get_results_list(RESULTS_TO_PROCESS_PATH)
for file in results_file_list:
    converted_data = process.convert_to_utf8_data(file)
    with open(get_converted_results_path(file), "wb") as output_file:
        output_file.write(converted_data)
