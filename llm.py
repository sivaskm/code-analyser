from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
import os


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_file_description(code):
    system_msg = (
        "You are an expert in understanding any large codebase. "
        "Now you are tasked with extracting valuable information from a file which is part of a large codebase. "
        "Give response in proper json format with no other text. Don't put any prefix or markdwon in the resoponse. Give pure json string."
    )

    model = genai.GenerativeModel("models/gemini-1.5-flash",
                                system_instruction=system_msg,
                                generation_config={"response_mime_type": "application/json"})

    prompt = f"""I have extracted code from a file and provided it under 'CODE'.
    Extract useful information from the following code and represent it in JSON format. 
    For each function, include the function name, description, and set the method type to "function." 
    For all other elements, set the type to "other."
    Your description should be easily understandable by a junior developer.
    Give detailed explanation about each component from the code.
    For each function, you should explain that function line by line. 

    ### Example Code
    ```javascript
    function add(a, b) {{
        return a + b;
    }}

    const PI = 3.14;

    ### Example Output
    [
        {{
            "name": "add",
            "description": "This function adds two numbers",
            "method_type": "function"
        }},
        {{
            "name": "PI",
            "description": "This is a constant value",
            "type": "other"
        }}
    ]

    ### CODE
    {code}
    """
    return model.generate_content(prompt).text


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_file_sequence(files):
    system_msg = (
    "You are an expert in understanding any large codebase. "
    "Now you are tasked with training your junior developer to make him understand the code. "
    "As a first step, you should give him a file sequence, by following the codebase in that order "
    "which he should be able to understand the code better. "
    "Give response in simple this JSON format: {'files_to_consider': ['list of files']}"
    "Consider only the files related to development. "
    "Don't consider files which are related to deployment and other dependency managers such as Dockerfile, pyproject.toml etc.,"
    "Deployment and dependency related files should be completed avoided."
    )

    model = genai.GenerativeModel("models/gemini-1.5-flash",
                                system_instruction=system_msg,
                                generation_config={"response_mime_type": "application/json"})

    prompt = (
    "The file names extracted from a large codebase is provided before 'FILE LIST'. "
    "You read the filenames and get yourself familiar with the project structure. "
    "Arrange all files in an order, using which anyone can start reading the code. "
    "For example if you tell to start from 'main.py' file and then move to 'handler.py' "
    "You should give list in this order: ['main/py', 'handler.py']"
    "Ouptut file list should be arranged in a way that if I use the list, "
    "I should be able to understand the code easier. "
    "For example I start from main.py file and this file has some dependecy with "
    "handler.py file. Then I go to that file for understanding the codebase. "
    "So the sequence would look like [main.py, handler.py] "
    "You should understand the purpose of a file solely by reading file name. "
    f"FILE LIST: {files}"
    )

    return model.generate_content(prompt).text