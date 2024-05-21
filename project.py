import argparse
import json
import yaml
import xmltodict
from PyQt5 import QtWidgets
import sys
import concurrent.futures

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

class ConverterApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.input_label = QtWidgets.QLabel('Input File', self)
        self.input_label.move(20, 20)

        self.input_path = QtWidgets.QLineEdit(self)
        self.input_path.move(20, 40)
        self.input_path.resize(280, 20)

        self.output_label = QtWidgets.QLabel('Output File', self)
        self.output_label.move(20, 80)

        self.output_path = QtWidgets.QLineEdit(self)
        self.output_path.move(20, 100)
        self.output_path.resize(280, 20)

        self.convert_button = QtWidgets.QPushButton('Convert', self)
        self.convert_button.move(20, 140)
        self.convert_button.clicked.connect(self.convert_files)

        self.setGeometry(300, 300, 320, 200)
        self.setWindowTitle('File Converter')
        self.show()

    def convert_files(self):
        input_file = self.input_path.text()
        output_file = self.output_path.text()
        if input_file.endswith('.json'):
            data = load_json(input_file)
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            data = load_yaml(input_file)
        elif input_file.endswith('.xml'):
            data = load_xml(input_file)
        else:
            print("Unsupported input file format")
            return

        if data:
            if output_file.endswith('.json'):
                save_json(data, output_file)
            elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
                save_yaml(data, output_file)
            elif output_file.endswith('.xml'):
                save_xml(data, output_file)
            else:
                print("Unsupported output file format")

class ConverterApp(QtWidgets.QWidget):

    def convert_files(self):
        input_file = self.input_path.text()
        output_file = self.output_path.text()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.convert, input_file, output_file)
            future.add_done_callback(self.show_result)

    def convert(self, input_file, output_file):
        if input_file.endswith('.json'):
            data = load_json(input_file)
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            data = load_yaml(input_file)
        elif input_file.endswith('.xml'):
            data = load_xml(input_file)
        else:
            return "Unsupported input file format"

        if data:
            if output_file.endswith('.json'):
                save_json(data, output_file)
            elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
                save_yaml(data, output_file)
            elif output_file.endswith('.xml'):
                save_xml(data, output_file)
            else:
                return "Unsupported output file format"
        return "Conversion completed"

    def show_result(self, future):
        result = future.result()
        print(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())