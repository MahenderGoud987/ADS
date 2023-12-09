import os

current_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(current_dir)
file_path = os.path.join(PROJECT_ROOT, 'app.properties')


def read_property(file_path):
    separator = "="
    dictionary = {}
    # logging.info(f"reading property file from path {file_path}")
    try:
        with open(file_path, 'r') as f:

            for line in f:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)

                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    dictionary[name.strip()] = value.strip()
    except Exception as error:
        # logging.info(f"unable to read properties file {error}")
        return f"unable to read properties file {error}"
    else:
        # logging.info(f"properties dictionary {dictionary}")
        return dictionary


properties = read_property(file_path)
