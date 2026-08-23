import json
import sys

def flatten_json(obj, prefix="", result=None, current_depth=0):
    if result is None:
        result = {}
    
    if current_depth > 20:
        raise ValueError("Maximum nesting depth of 20 levels exceeded.")

    for key, value in obj.items():
        new_key = f"{prefix}.{key}" if prefix else key
        
        if isinstance(value, dict) and value:
            flatten_json(value, new_key, result, current_depth + 1)
        elif isinstance(value, dict) and not value:
            continue
        else:
            result[new_key] = value
            
    return result

def process_input(json_str):
    data = json.loads(json_str)
    flattened = flatten_json(data)
    sorted_flattened = {key: flattened[key] for key in sorted(flattened.keys())}
    return json.dumps(sorted_flattened, separators=(',', ':'))

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        print(process_input(input_data))
