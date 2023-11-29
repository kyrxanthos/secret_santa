import os

def read_env_file(file_path='.env'):
    """
    Read and parse the contents of a .env file.

    Args:
    - file_path (str): Path to the .env file. Default is '.env'.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            os.environ[key] = value