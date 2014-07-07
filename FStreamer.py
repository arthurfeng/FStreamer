'''
Created on 2014-7-3

@author: fengjian
'''

import os
from src import ffmpeg, segmenter

VIDEOFORMAT = [".ts", ".mp4", ".mkv"]

root = raw_input("Input Your Contents Or Folder Name: ")
            

def run(filepath):
    
    ffmpeg.ffmpeg(filepath)
    segmenter.segmenter(filepath)   

if __name__ == '__main__':
    
    if os.path.isfile(root):
        print "Transcoding %s to HLS..." % root
        run(root)
    else:
        for dirName, subdirList, fileList in os.walk(root): 
            for fname in fileList:
                name, extension = os.path.splitext(fname)
                if extension in VIDEOFORMAT:
                    print "Transcoding %s to HLS..." % fname
                    #run("%s\%s" % (dirName, fname))
                    run(os.path.join(dirName, fname))