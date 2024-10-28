import ast

def read_mixed_lists_from_file(file_path):
    with open(file_path, 'r') as file:
        tuples = []
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            if line:  # If the line is not empty
                # Safely evaluate the list string
                try:
                    parsed_list = ast.literal_eval(line)
                    if isinstance(parsed_list, tuple):
                        parsed_list = list(parsed_list)
                    if not isinstance(parsed_list, list):
                        parsed_list = [parsed_list]
                except:
                    parsed_list = [line]
                # Append to the result list
                tuples.append(parsed_list)
    return tuples

def read_single_from_file(file_path):
    with open(file_path, 'r') as file:
        lists = []
        for line in file:
            
            line = line.strip()
            if line:
                try:
                    line = ast.literal_eval(line)
                except:
                    pass
                lists.append(line)
    return lists

def read_plain_text_from_file(file_path):
    with open(file_path, 'r') as file:
        lists = []
        for line in file:
            line = line.strip()
            if line:
                lists.append([line])
    return lists

if __name__ == '__main__':
    # Example Usage
    print(read_mixed_lists_from_file('grade_func/input/hw12_q_9.txt'))
    print(read_single_from_file('grade_func/output/hw12_q_9.txt'))