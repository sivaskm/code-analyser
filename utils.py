import json
import os

def read_file(file_path):
    """Reads the content of a file.

    Args:
        file_path: The path to the file.

    Returns:
        The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
        return None


def save_json_from_string(json_string, file_path):
  """
  Takes a JSON string, converts it to a dictionary, and saves it as a JSON file.

  Args:
    json_string: The JSON string to convert and save.
    file_path: The path to the file where the JSON data will be saved.
  """
  try:
    data = json.loads(json_string)
    with open(file_path, 'w') as f:
      json.dump(data, f, indent=4)
    print(f"JSON data saved to {file_path}")
  except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

    
    
def get_completed_file_paths(result_folder):
  """
  Lists completed file paths by reading the result folder.

  Args:
    result_folder: The path to the folder containing the results.

  Returns:
    A list of completed file paths with a prefix.
  """
  completed_file_paths = []
  for filename in os.listdir(result_folder):
    if filename.endswith(".json"):
      file_path = os.path.join(result_folder, filename)
      completed_file_paths.append(f"sensei/sensei-main/{filename[:-5]}")
  return completed_file_paths

def make_dir(dir):
   if not os.path.exists(dir):
    os.makedirs(dir)

def get_file_list(dir):
    file_paths = []

    for root, _, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_path = file_path.replace(dir, "")
            file_paths.append(file_path)
    return file_paths


