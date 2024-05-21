import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data conversion program')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()
    return args.input_file, args.output_file

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    print(f"Input File: {input_file}")
    print(f"Output File: {output_file}")
