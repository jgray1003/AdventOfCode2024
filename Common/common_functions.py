
def read_file(file_name, line_by_line=True, example_file=False):

    input_dir = 'InputData' if not example_file else 'ExampleInputData'
    file = open(f"{input_dir}/{file_name}")

    if line_by_line:
        return file.readlines()
    else:
        return file.read()

def convert_strs_to_ints(arr):
    return [int(item) for item in arr]