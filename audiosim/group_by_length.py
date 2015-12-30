'''
This module contains filter functions that reduces the set of audio files to run the compare function with
Author: Tim Huynh
'''

import wave, contextlib, os

def quickSort(array, low, high):
    if low >= high:
        return

    pivot = array[low].fileLength
    i = low
    j = high

    while i <= j :
        while array[i].fileLength < pivot and i <= high :
            i = i + 1
        while array[j].fileLength > pivot and j >= low :
            j = j - 1
        
        if i <= j :
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i = i + 1
            j = j - 1

    quickSort(array, low, j)
    quickSort(array, i, high)


class Wav:
    def __init__(self, filepath, fileLength):
        self.filepath = filepath
        self.fileLength = fileLength

def get_all_files(path):
    fl = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for f in filenames:
            f = dirpath + '/' + f
            fl.append(f)
        break
    return fl

# gets the time length of the file in seconds
def get_file_length(file):
    fileLength = 0
    with contextlib.closing(wave.open(file,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        fileLength = frames / float(rate)
    return fileLength

# take directory and create a list of groups of files that are similar in size
def group_by_length(directory):
    filesDetails = []
    fileList = get_all_files(directory)
    for file in fileList:
        length = get_file_length(file)
        wavDetails = Wav(file, length)
        filesDetails.append(wavDetails)

    quickSort(filesDetails, 0, len(filesDetails) - 1)   # comment out this line for unsorted list
    return filesDetails


if __name__ == '__main__':
    # run script py group_by_length.py {working_dir}
    workingDir = str(sys.argv[1])
    wavDescriptors = group_by_length(workingDir)
    print(wavDescriptors)

    # can run functions on wavDescriptors here
