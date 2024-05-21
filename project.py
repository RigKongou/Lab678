import argparse
import json
import yaml
import xmltodict

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data conversion program')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()
    return args.input_file, args.output_file

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing JSON file: {e}")

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Error reading YAML file: {e}")
        return None

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing YAML file: {e}")

def load_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
        return data
    except Exception as e:
        print(f"Error reading XML file: {e}")
        return None

def save_xml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            xml_data = xmltodict.unparse(data, pretty=True)
            file.write(xml_data)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing XML file: {e}")

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    if input_file.endswith('.json'):
        data = load_json(input_file)
        if data:
            print("JSON data loaded successfully")
            if output_file.endswith('.json'):
                save_json(data, output_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
        if data:
            print("YAML data loaded successfully")
            if output_file.endswith('.yml') or output_file.endswith('.yaml'):
                save_yaml(data, output_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
        if data:
            print("XML data loaded successfully")
            if output_file.endswith('.xml'):
                save_xml(data, output_file)