import os
from datetime import datetime
import time
from mimetypes import MimeTypes
import eyeD3

class file:
    pass

class fileinfo:

    def basic(self,filepath):
        f=file()
        f.created=time.ctime(os.stat(filepath).st_atime)
        f.last_modified=""
        f.mime = MimeTypes().guess_type(filepath)[0]
        f.extension=os.path.splitext(filepath)[1]
        f.name=os.path.basename(filepath)
        f.path=filepath
        f.meta=self.metadata(f)
        return f.__dict__
    
    def metadata(self,f):
        if f.extension==".mp3":
            return self.videoinfo(f.path)
        return {}

    def mp3info(self,path):
        trackInfo = eyeD3.Mp3AudioFile(path)
        tag = trackInfo.getTag()
        tag.link(path) 
        tag.getArtist()
        metadata={}
        metadata['album']=tag.getAlbum()
        metadata['track']=tag.getTitle()
        metadata['length']=trackInfo.getPlayTimeString()
        metadata['release_year']=tag.getYear()
        return metadata
    def videoinfo(self,path):
        return ""

