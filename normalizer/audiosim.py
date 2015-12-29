
# coding: utf-8

# In[ ]:

import os


# In[ ]:

import numpy as np


# In[ ]:

import librosa


# #### prototyping

# In[ ]:

directory="/Users/crosskonaftw/Documents/repos/audiosim/normalizer/"


# In[ ]:

y, sr = librosa.core.load(directory+"source_files/file1.wav", sr=44100, mono=True, offset=0, duration=10)


# In[ ]:

print "y=",y


# In[ ]:

print "sr=",sr


# In[ ]:

np.save(directory+"/output_files/output.npy",y)


# #### end prototyping

# #### begin looped version

# In[ ]:

filename_array=os.listdir(directory+"/source_files") #load files


# In[ ]:

print filename_array #check


# In[ ]:

song_count=len(filename_array) #assign count var
print song_count #check
print type(filename_array) #check + ref

#working, leave me alone, currently inactive
for i in filename_array:
    print "/Users/crosskonaftw/Downloads/audiosim/source_files/"+i
    temp, sr=librosa.core.load("/Users/crosskonaftw/Downloads/audiosim/source_files/"+i, sr=44100, mono=True, offset=0, duration=10)
# In[ ]:

output=np.zeros((song_count,441000)) #create array


# In[ ]:

#testing

#enum example
#for idx, val in enumerate(ints):
#    print idx, val
    
#load matrix with librosa returned data
for idx, i in enumerate(filename_array):
    #print "/Users/crosskonaftw/Downloads/audiosim/source_files/"+i
    temp, sr=librosa.core.load(directory+"/source_files/"+i, sr=44100, mono=True, offset=0, duration=10)
    print idx, i
    output[idx]=temp


# In[ ]:

print output #look at the output


# In[ ]:

#create final file
np.save(directory+"/output_files/newmatrix.npy",output)


# In[ ]:

print "done"


# In[ ]:



