
def read_file(file_name, example_file=False):

    input_dir = 'InputData' if not example_file else 'ExampleInputData'
    file = open(f"{input_dir}/{file_name}")
    return file.readlines()

def convert_strs_to_ints(arr):
    return [int(item) for item in arr]