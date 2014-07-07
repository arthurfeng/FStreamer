'''
Created on 2014-7-3

@author: fengjian
'''
import os

SEGMENTERPATH = r"bin\segmenter.exe"

class Segmenter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def cmd(self, filepath):
        
        dirname, filename = os.path.split(filepath)
        filename, extension = os.path.splitext(filename)
        if os.path.exists("m3u8\%s.m3u8" % filename):
            cmd = ""
        else:
            os.makedirs(r"segments/%s" % filename)
            cmd = r'''%s -i "mpegts\%s.ts" -d 10 -x "m3u8\%s.m3u8" -o "segments\%s\%s"''' % (SEGMENTERPATH, filename, 
                                                                                             filename, filename, filename)
        return cmd
        
    def start(self, cmd):
        
        print cmd
        result = os.system(cmd)
        
def segmenter(filepath):
    
    SEGMENTER = Segmenter()
    cmd = SEGMENTER.cmd(filepath)
    SEGMENTER.start(cmd)