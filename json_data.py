import json

def get_json_data(filepath):
    try:
        with open(filepath) as file:
            json_data = file.read()
            json_data = json.loads(json_data)
            return json_data
        
    except UnicodeDecodeError:
        print("Trying to read this file caused a UnicodeDecodeError, is", filepath, "the correct file?")
        return ""
    except json.JSONDecodeError:
        print("Trying to read this file caused a JSONDecodeError, is", filepath, "the correct file?")
        return ""
    except ValueError:
        print("Trying to read this file caused an unknown error, is", filepath, "the correct file?")
        return ""
    
def contains_key(object, key):
    key = key
    return str(object).find(key) != -1