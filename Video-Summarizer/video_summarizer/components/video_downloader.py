## Program snippet to downlaod video and save to the system 

import os, sys, requests
from pytube import YouTube 
from video_summarizer.exceptions import CustomException 
from video_summarizer.logger import logger 

class Video_Downloader:
    def __init__(self,url:str,save_path:str)->None:
        self.url = url 
        self.save_path = save_path 
    
    def download(self)->None | str:
        try:
            if 'youtu' in self.url:
                return self._download_youtube()
            else:
                return self._download_other()
        except Exception as e:
            raise CustomException(e,sys)   
        
    def _download_youtube(self):
        try:
            yt = YouTube(self.url)
            video = yt.stream.first()
            video.download(self.save_path) 
            logger.info(f"Youtube video downloaded successfully at {os.path.join(self.save_path,video.default_filename)}") 
            return os.path.join(self.save_path,video.default_filename)
        except Exception as e:
            raise CustomException(e,sys)
        
    def _download_other(self):
        try:
            response = requests.get(self.url, stream=True)
            filename = self.url.split("/")[-1]
            with open(os.path.join(self.save_path, f"{filename}"),'wb') as f:
                for chunk in response.iter_content(chunk_size=4096):
                    f.write(chunk)    
                logger.info(f"Video download completed at {os.path.join(self.save_path,filename)}")
                return os.path.join(self.save_path,filename) 
        except Exception as e:
            raise CustomException(e,sys) 
        
            

