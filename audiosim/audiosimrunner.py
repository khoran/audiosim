import os
import sys

def get_filepaths(directory):
	file_paths = []

	for root, directories, file in os.walk(directory):
		for filename in files:
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	return file_paths


workingDir = str(sys.argv[0])
print workingDir
print str(sys.argv)

all_file_paths = get_filepaths(workingDir)
print all_file_paths

