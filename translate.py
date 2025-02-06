import os
import re
import requests
import json

# Replace YOUR_AUTH_KEY with your Deepl API authentication key
AUTH_KEY = ""

# Replace FOLDER_PATH with the path to your .po file
FILE_PATH = ""

# Define the API endpoint and parameters
DEEPL_URL = "https://api-free.deepl.com/v2/translate"

def escape_quotes(text):
    """Ensure double quotes inside text are escaped."""
    return text.replace('"', '\\"')

def extract_messages(file_contents):
    """Extract msgid and msgstr from the .po file."""
    messages = []
    in_message = False
    message_id = ""
    message_str = ""

    for line in file_contents.splitlines():
        if line.startswith("msgid "):
            message_id = line[6:].strip().strip('"')
            in_message = True
        elif line.startswith("msgstr "):
            message_str = line[7:].strip().strip('"')
            in_message = False
            messages.append((message_id, message_str))
        elif in_message:
            message_id += " " + line.strip().strip('"')

    return messages

def replace_placeholders(text):
    """Replace variables inside {} and guillemets (« ») with placeholders."""
    variables = re.findall(r"{[^}]*}", text)
    placeholder_map = {var: f"__VAR{idx}__" for idx, var in enumerate(variables)}

    # Also replace guillemets
    placeholder_map["«"] = "__LEFT_GUILLEMET__"
    placeholder_map["»"] = "__RIGHT_GUILLEMET__"

    for var, placeholder in placeholder_map.items():
        text = text.replace(var, placeholder)

    return text, placeholder_map

def restore_placeholders(text, placeholder_map):
    """Restore original placeholders after translation."""
    for var, placeholder in placeholder_map.items():
        text = text.replace(placeholder, var)

    return text

def translate_text(text):
    """Translate text using DeepL API while preserving placeholders."""
    if not text or text.isspace():
        return text  # Skip empty strings

    text, placeholder_map = replace_placeholders(text)

    params = {
        "auth_key": AUTH_KEY,
        "text": text,
        "source_lang": "FR",
        "target_lang": "ES",
        "preserve_formatting": "1",
        "tag_handling": "xml",
        "ignore_tags": "br",
        "formality": "default",
    }

    print(f"Translating: {text}") 

    response = requests.post(DEEPL_URL, data=params)
    
    print(f"Response Status: {response.status_code}")  
    print(f"Response Text: {response.text}")  

    if response.status_code == 200:
        translated_text = response.json()["translations"][0]["text"]
        return restore_placeholders(translated_text, placeholder_map)
    else:
        print(f"Translation failed: {response.status_code}, {response.text}")
        return text  # Return original text in case of failure

def translate_file(file_path):
    """Read, translate, and update the .po file."""
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()

    messages = extract_messages(file_contents)
    translated_messages = []

    for message_id, message_str in messages:
        translated_msgstr = translate_text(message_id)
        translated_messages.append((escape_quotes(message_id), escape_quotes(translated_msgstr)))

    # Rebuild the .po file with translations
    output_lines = []
    for msgid, msgstr in translated_messages:
        output_lines.append(f'msgid "{msgid}"')
        output_lines.append(f'msgstr "{msgstr}"\n')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print("Translation complete!")

# Run the function
translate_file(FILE_PATH)

