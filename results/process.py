import codecs
import glob
from chardet.universaldetector import UniversalDetector

def get_results_list(path):
    return glob.glob(path + "/*R*.json", recursive=False)

## source: https://stackoverflow.com/questions/191359/how-to-convert-a-file-to-utf-8-in-python
def get_src_encoding(filename):
    detector = UniversalDetector()
    with open(filename, "rb") as data:
        detector.reset()
        for line in data:
            detector.feed(line)
            if detector.done: break
        detector.close()
    return detector.result["encoding"]

def convert_to_utf8_data(input_file_path):
    try:
        src_encoding = get_src_encoding(input_file_path)
        if src_encoding == "ISO-8859-1":
            src_encoding = "utf-16-le"
        input_file = codecs.open(input_file_path, "rb", encoding=src_encoding)
        decoded_data = input_file.read()
        encoded_data = codecs.encode(decoded_data, encoding="utf-8")
        return encoded_data
    except UnboundLocalError:
        SystemExit()
    finally:
        input_file.close()
