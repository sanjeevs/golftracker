#
# File manipulations.
import pathlib
import os
import csv

def basename(fname):
	"""
	Return the base name of windows file name. 

	>>> basename('c:/a/b/c.txt')
	'c.txt'

	>>> basename('a.txt')
	'a.txt'

	"""
	p = pathlib.Path(fname)
	return os.path.basename(p)

def search_file(search_dir, fname):
	"""
	Check whether the file exists in the search dir.

	>>> search_file(".", "file_utils.py")
	'.\\\\file_utils.py'

	"""
	p = pathlib.Path(fname)
	f = os.path.join(search_dir, fname)
	if os.path.exists(f):
		return f
	else:
		return None

def write_to_csv(data, file_name, header=None):
    """
    Writes a list of lists to a CSV file, with an optional header.

    :param data: List of lists to be written to the CSV file.
    :type data: list[list]
    :param file_name: Name of the CSV file to be created.
    :type file_name: str
    :param header: Optional header row for the CSV file.
    :type header: list or None
    """
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(data)


def read_from_csv(file_name, has_header=False):
    """
    Reads data from a CSV file and returns it as a list of lists. Optionally reads the first row as a header.

    :param file_name: Name of the CSV file to be read.
    :type file_name: str
    :param has_header: Specifies whether the CSV file has a header row.
    :type has_header: bool
    :return: Tuple containing the header (if present) and the data.
    :rtype: (list, list[list])
    """
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        if has_header:
            header = next(reader)  # Read the first row as header
        else:
            header = None

        data = [row for row in reader]

    return header, data