'''
This module contains filter functions that reduces the set of audio files to run the compare function with
Author: Tim Huynh
'''

import wave, contextlib, os

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

    return filesDetails


if __name__ == '__main__':
    #fileLength = get_file_length("D:/My Documents/Projects/audiosim/resources/LimbuProg30Sec.wav")
    #print(fileLength)
    groups = group_by_length("D:/My Documents/Projects/audiosim/resources")
    print(groups)