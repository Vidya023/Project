## This program snippet is for converting downloaded video to ausio and respective transcripts 

import whisper 
import tempfile 
import os 
import sys 
import warnings
from moviepy.editor import VideoFileClip
from dataclasses import dataclass
from video_summarizer.logger import logger 
from video_summarizer.exceptions import CustomException  


@dataclass
class Config():
        codec: str = 'pcm_s16le'
        bitrate: str = '16k'
        output_dir_name: str = 'transcript_text' 
        

class video_to_text:
    def __init__(self, config:Config):
        try:
            self.codec = config.codec
            self.bitrate = config.bitrate
            self.output_dir = config.output_dir_name
            
        except Exception as e:
            raise CustomException(e, sys)    
        
    def get_audio(self,paths)->dict:
        try: 
            print(f"Video path = {paths}")    
            temp_dir = tempfile.gettempdir()
            audio_paths = {}
            for path in paths:
                filename = os.path.basename(path).split('.')[0]
                logger.info(f"Extracting audio from file {os.path.basename(path)}........")
                output_path = os.path.join(temp_dir, f"{filename}.wav") 
                video_clip = VideoFileClip(path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(output_path, codec=self.codec, bitrate=self.bitrate) 
                audio_clip.close()
                video_clip.close()
                audio_paths[path] = output_path 
            return audio_paths
        except Exception as e:
            raise CustomException(e, sys)

    def write_transcript(self,audio_path,text_path,transcribe:callable):
        try:  
            logger.info(f"Generating transcript for {os.path.basename(audio_path)} audio... This might take a while.")  
            warnings.filterwarnings('ignore') 
            result = transcribe(audio_path)
            warnings.filterwarnings('default')
            logger.info("Writing transcript for video.")
            with open(text_path,'w',encoding='utf-8') as f:
                f.write(result['text']) 
            return result     
        except Exception as e:
            raise CustomException(e, sys)
    def get_transcript(self,audio_path:list,output_text:bool,output_dir:str,transcribe:callable):
        try:
            text_path = output_dir if output_text else tempfile.gettempdir()
            for path, audio_path in audio_path.items():
                filename = os.path.basename(path).split('.')[0]
                text_path = os.path.join(text_path,f"{filename}.txt")
                result = self.write_transcript(audio_path,text_path,transcribe) 
            return result 
        except Exception as e:
            raise CustomException(e, sys)     

    def initiate_stt(self,video_path:str,model:str,srt:bool,verbose:bool,task:str): 
        print(f"Video path = {video_path}") 
        os.makedirs(self.output_dir,exist_ok=True)
        if model.endswith('.en'):
            print(f"{model} is English model")
        model = whisper.load_model(model)
        audio = self.get_audio(video_path)
        subtitle = self.get_transcript(audio,srt,self.output_dir,
                                         lambda audio_path: model.transcribe(audio_path,
                                                                             verbose=verbose,task=task)) 
        return subtitle     

