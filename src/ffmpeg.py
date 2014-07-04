'''
Created on 2014-7-3

@author: fengjian
'''

import os

TSFOLDER = "mpegts"
FFMPEGFOLDER = r"bin\ffmpeg.exe"

class FFMPEG(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def cmd(self, filepath):
        
        dirname, filename = os.path.split(filepath)
        filename, extension = filename.split(".")
        if os.path.exists("mpegts\%s.ts" % filename):
            return ""
        else:
            return '''%s -i "%s" -vcodec h264 -acodec aac -strict -2 "%s\%s.ts"''' % (FFMPEGFOLDER, filepath, TSFOLDER, filename)
    
    def run(self, cmd):
        
        result = os.system(cmd)
    
def ffmpeg(filepath):
    
    Trans = FFMPEG()
    cmd = Trans.cmd(filepath)
    Trans.run(cmd)

        