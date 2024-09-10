from utils import read_file, save_json_from_string, get_completed_file_paths, make_dir, get_file_list
from llm import get_file_description, get_file_sequence
import os

CODE_DIR = "data/sensei-main/"
RESULT_DIR = "result"

file_list = get_file_list(CODE_DIR)
file_sequence = get_file_sequence(file_list)
save_json_from_string(file_sequence, "sequence.json")

completed = get_completed_file_paths(RESULT_DIR)

for root, _, files in os.walk(CODE_DIR):
    for file in files:
        try:
            if file not in completed:
                file_path = os.path.join(root, file)
                print(file_path)
                code = read_file(file_path)
                if code:
                    desc = get_file_description(code)
                    dest = os.path.join(file_path.replace("data", "result", 1) + ".json")
                    dest_dir = os.path.dirname(dest)
                    make_dir(dest_dir)
                    save_json_from_string(desc, dest)
                    
        except Exception as e:
            print(e, file_path)
            continue
        
