
def read_file(file_name, line_by_line=True, example_file=False):

    input_dir = 'InputData' if not example_file else 'ExampleInputData'
    file = open(f"{input_dir}/{file_name}")

    if line_by_line:
        return file.readlines()
    else:
        return file.read()

def read_file_to_2D_array(file_name, example_file=False):
    input_lines = read_file(file_name, example_file=example_file)

    arr = []
    for line in input_lines:
        arr.append(list(line.replace('\n', '')))
    return arr

def convert_strs_to_ints(arr):
    return [int(item) for item in arr]

def print_friendly_2D_arr(arr, delimiter=''):
    for row in arr:
        row_str = ''
        for col in row:
            row_str += col + delimiter
        if delimiter != '':
            row_str = row_str[:-len(delimiter)]
        print(f'{row_str}')

def tuples_equal(tup_1, tup_2):
    return tup_1[0] == tup_2[0] and tup_1[1] == tup_2[1]